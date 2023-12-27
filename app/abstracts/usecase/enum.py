from enum import Enum


class ErrorsUseCaseEnum(str, Enum):
    DETAILS_NOT_FOUND = "{model} details not found."
    NOT_FOUND = "{model} not found."
    ALREADY_REGISTERED = "{model} already registered."
    PARAMETERS_NOT_FOUND = "Parameters not found {model}"
