from datetime import datetime, timedelta

from fastapi import Request, HTTPException, status

from app.abstracts.usecase.base_usecase import (
    BaseHtmlRenderTemplate,
)
from app.modules.notifications import schema
from app.modules.notifications.abstracts.base_notification_usecase import (
    BaseNotificationUseCase,
)
from app.modules.notifications.enum import (
    NotificationTypesEnum,
    NotificationTemplateFilesEnum,
    NotificationMessagesEnum,
)


class SendEmailFirstContactUseCase(BaseNotificationUseCase, BaseHtmlRenderTemplate):
    _template_name = NotificationTemplateFilesEnum.EMAIL_FIRST_CONTACT.value
    _type = NotificationTypesEnum.EMAIL_FIRST_CONTACT.value
    _payload: schema.SendEmailFirstContactSchema

    def __init__(self, payload: schema.SendEmailFirstContactSchema, request: Request):
        super().__init__(payload=payload)
        self._request = request

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

    async def execute(self):
        await self._validate()
        template = await self._get_template_response(self._payload.dict())
        notification_db = await self._register_notification()
        return schema.GetSimpleNotificationSchema.from_orm(notification_db)
