from datetime import datetime
from typing import Optional

from app.abstracts.schema.base_schema import BaseSchema
from app.modules.core.validators import (
    ValidateEmailSchema,
    ValidateIpAddressSchema,
    ValidatePhoneNumberSchema,
    ValidateEmptyValuesSchema,
)
from app.modules.notifications.enum import NotificationTypesEnum


class GetNotificationSchema(BaseSchema):
    id: int
    uuid: str
    type: NotificationTypesEnum
    ip_address: str
    payload: dict
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class GetSimpleNotificationSchema(BaseSchema):
    uuid: str
    type: NotificationTypesEnum
    created_at: Optional[datetime]


class CreateNotificationSchema(BaseSchema, ValidateIpAddressSchema):
    type: NotificationTypesEnum
    ip_address: str
    payload: dict


class SendEmailFirstContactSchema(
    BaseSchema,
    ValidateEmailSchema,
    ValidateIpAddressSchema,
    ValidateEmptyValuesSchema,
    ValidatePhoneNumberSchema,
):
    ip_address: str
    from_email: str
    text: str
    phone_number: Optional[str]
