from abc import ABCMeta
from enum import Enum

from fastapi import HTTPException, status
from fastapi_camelcase import CamelModel


async def clean_none_values_dict(kwargs: dict) -> dict:
    copy_dict = kwargs.copy()
    for key, value in kwargs.items():
        if value is None:
            del copy_dict[key]
        if value is not None and isinstance(value, list) and len(value) == 0:
            del copy_dict[key]
    return copy_dict


class ErrorsEnum(str, Enum):
    PARAMETERS_NOT_FOUND = "{model}: Parameters not found."


class BaseUtilsUseCase(metaclass=ABCMeta):
    _payload: CamelModel
    _payload_clean: dict
    _model_name: str

    async def _validate_values_payload(self):
        clean_dict = await clean_none_values_dict(self._payload.dict())
        if len(clean_dict.keys()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorsEnum.PARAMETERS_NOT_FOUND.format(model=self._model_name),
            )
        self._payload_clean = clean_dict
