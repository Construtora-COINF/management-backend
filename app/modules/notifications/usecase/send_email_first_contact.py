from datetime import datetime, timedelta
from fastapi import Request, HTTPException, status

from app.abstracts.usecase.base_usecase import (
    BaseHtmlRenderTemplate,
)
from app.config.settings import get_settings
from app.modules.core.enum import FormatDatetimeEnum
from app.modules.core.utils import remove_html_text
from app.modules.notifications import schema
from app.modules.notifications.abstracts.base_notification_usecase import (
    BaseNotificationUseCase,
)
from app.modules.notifications.enum import (
    NotificationTypesEnum,
    NotificationTemplateFilesEnum,
    NotificationMessagesEnum,
)
from app.services.amazon_ses import AmazonSimpleEmailService


class SendEmailFirstContactUseCase(BaseNotificationUseCase, BaseHtmlRenderTemplate):
    __setting = get_settings()
    _template_name = NotificationTemplateFilesEnum.EMAIL_FIRST_CONTACT.value
    _type = NotificationTypesEnum.EMAIL_FIRST_CONTACT.value
    _email_from = __setting.EMAIL_NO_REPLY
    _email_to = __setting.EMAIL_CONTACT
    _payload: schema.SendEmailFirstContactSchema

    def __init__(self, payload: schema.SendEmailFirstContactSchema, request: Request):
        super().__init__(payload=payload)
        self._request = request
        self._amazon_ses = AmazonSimpleEmailService()

    async def _validate(self):
        one_hour_ago = datetime.now() - timedelta(hours=1)
        notification = await self._repository.filter(
            get_first=True,
            ip_address=self._payload.ip_address,
            created_at__gte=one_hour_ago,
        )
        if notification:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=NotificationMessagesEnum.TIMEOUT_SEND_EMAIL_FIRST_CONTACT,
            )

    async def _register_notification(self):
        notification_db = await self._repository.create(
            dict(
                type=self._type,
                ip_address=self._payload.ip_address,
                payload=self._payload.dict(),
            )
        )
        return notification_db

    async def _get_template(self, data: dict):
        template = await self._render_template_response(data)
        template_text = await remove_html_text(bytes(template.body).decode("UTF-8"))
        return template, template_text

    async def _send_email(self, data, send_at: datetime):
        data["send_at"] = send_at.strftime(FormatDatetimeEnum.DATETIME_WITH_TEXT.value)
        template, template_text = await self._get_template(data)
        await self._amazon_ses.send_email(
            from_email=self._email_from,
            to_email=self._email_to,
            subject=NotificationMessagesEnum.value.format(
                from_email=self._payload.from_email
            ),
            body_html=bytes(template.body).decode("UTF-8"),
            body_text=template_text,
        )

    async def execute(self):
        await self._validate()
        notification_db = await self._register_notification()
        await self._send_email(self._payload.dict(), notification_db.created_at)
        return schema.GetSimpleNotificationSchema.from_orm(notification_db)
