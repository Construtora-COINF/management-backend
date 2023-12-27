from abc import ABCMeta

from fastapi_camelcase import CamelModel
from pydantic import validator

from app.modules.core.enum import MessageEnum
from app.modules.core import utils


class ValidateEmptyValuesSchema(CamelModel, metaclass=ABCMeta):
    @validator("name", "text", check_fields=False)
    def validate_empty_values(cls, value):
        if len(value) == 0:
            raise ValueError(MessageEnum.INVALID_EMPTY_VALUE.value)
        return value


class ValidateEmailSchema(CamelModel, metaclass=ABCMeta):
    @validator("from_email", "email", check_fields=False)
    def validate_email(cls, value):
        if not utils.valid_format_email(value):
            raise ValueError(MessageEnum.INVALID_EMAIL.format(value=value))
        return value


class ValidateIpAddressSchema(CamelModel, metaclass=ABCMeta):
    @validator("ip_address", check_fields=False)
    def validate_ip_address(cls, value):
        if not utils.is_valid_ip_address(value):
            raise ValueError(MessageEnum.INVALID_IP_ADDRESS.format(value=value))
        return value


class ValidatePhoneNumberSchema(CamelModel, metaclass=ABCMeta):
    @validator("phone_number", check_fields=False)
    def validate_phone_number(cls, value):
        if not utils.valid_format_phone_number(value):
            raise ValueError(MessageEnum.INVALID_PHONE_NUMBER.format(value=value))
        return value


class ValidatePasswordSchema(CamelModel, metaclass=ABCMeta):
    @validator("password", check_fields=False)
    def validate_password(cls, value):
        if not utils.valid_string_any_less_characters(value, 8):
            raise ValueError(MessageEnum.INVALID_PASSWORD_LESS_CHARACTER.value)
        if not utils.valid_string_with_number(value):
            raise ValueError(MessageEnum.INVALID_PASSWORD_WITH_NUMBER.value)
        if not utils.valid_string_with_upper_case(value):
            raise ValueError(MessageEnum.INVALID_PASSWORD_WITH_UPPER_CASE.value)
        if not utils.valid_string_with_lower_case(value):
            raise ValueError(MessageEnum.INVALID_PASSWORD_WITH_LOWER_CASE.value)
        if not utils.valid_string_with_special_character(value):
            raise ValueError(MessageEnum.INVALID_PASSWORD_WITH_SPECIAL_CHARACTER.value)
        return value
