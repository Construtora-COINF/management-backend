from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetNotificationSchema(CamelModel):
    id: int
    uuid: str
    type: str
    ip_address: str
    payload: dict
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class GetSimpleNotificationSchema(CamelModel):
    uuid: str
    type: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class CreateNotificationSchema(CamelModel):
    type: str
    ip_address: str
    payload: dict


class SendEmailFirstContactSchema(CamelModel):
    ip_address: str
    from_email: str
    text: str
    phone_number: Optional[str]
