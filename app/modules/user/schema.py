from datetime import datetime
from typing import Optional

from app.abstracts.schema.base_schema import BaseSchema
from app.modules.core.validators import (
    ValidateEmailSchema,
    ValidatePasswordSchema,
    ValidateEmptyValuesSchema,
)


class GetUserSchema(BaseSchema):
    id: int
    uuid: str
    email: str
    name: str
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class CreateUserSchema(
    BaseSchema, ValidateEmptyValuesSchema, ValidateEmailSchema, ValidatePasswordSchema
):
    name: str
    email: str
    password: str


class LoginUserSchema(BaseSchema, ValidateEmailSchema):
    email: str
    password: str


class JWTUserSchema(BaseSchema):
    uuid: str
    email: str
    access_token: str


class FilterUserSchema(BaseSchema):
    id: Optional[int]
    uuid: Optional[str]
    email: Optional[str]
    name: Optional[str]
    is_active: Optional[bool]
