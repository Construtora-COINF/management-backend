from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetUserSchema(CamelModel):
    id: int
    uuid: str
    email: str
    name: str
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class PostUserSchema(CamelModel):
    name: str
    email: str
    password: str


class UpdateUserSchema(CamelModel):
    name: str
    email: str
    password: str
    is_active: bool


class LoginUserSchema(CamelModel):
    email: str
    password: str


class JWTUserSchema(CamelModel):
    uuid: str
    email: str
    access_token: str


class SimpleMessageSchema(CamelModel):
    message: str


class FilterUserSchema(CamelModel):
    id: Optional[int]
    uuid: Optional[str]
    email: Optional[str]
    name: Optional[str]
    is_active: Optional[bool]
