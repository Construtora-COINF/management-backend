from enum import Enum


class FormatDatetimeEnum(str, Enum):
    DATETIME_WITH_TEXT = "%H:%M do dia %d de %B de %Y"


class MessageEnum(str, Enum):
    INVALID_EMAIL = "Invalid e-mail: {value}"
    INVALID_IP_ADDRESS = "Invalid ip address: {value}"
    INVALID_PHONE_NUMBER = "Invalid number: {value}"
    INVALID_PASSWORD_LESS_CHARACTER = "The password must contain at least 8 positions."
    INVALID_PASSWORD_WITH_NUMBER = (
        "The password must contain at least 1 digit, example: 0-9."
    )
    INVALID_PASSWORD_WITH_UPPER_CASE = (
        "Password must contain at least 1 uppercase letter, example: A-Z."
    )
    INVALID_PASSWORD_WITH_LOWER_CASE = (
        "Password must contain at least 1 lowercase letter, example: a-z."
    )
    INVALID_PASSWORD_WITH_SPECIAL_CHARACTER = (
        "Password must contain at least 1 symbol, example: ()[]{"
        r"}|\`~!@#$%^&*_-+=;:'\",<>./? . "
    )
    INVALID_EMPTY_VALUE = "It is not possible to register empty values"
