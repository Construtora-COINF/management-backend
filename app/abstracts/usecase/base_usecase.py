from abc import ABCMeta
from enum import Enum

from fastapi import HTTPException, Request, status

from app.abstracts.usecase.base_utils_usecase import BaseUtilsUseCase

from app.config.static_files import get_templates
from app.interfaces.usecase_interface import InterfaceUseCase


class ErrorsUseCaseEnum(str, Enum):
    DETAILS_NOT_FOUND = "{model} details not found."
    NOT_FOUND = "{model} not found."
    ALREADY_REGISTERED = "{model} already registered."
    PARAMETERS_NOT_FOUND = "Parameters not found {model}"


class BaseUseCaseValidDataBase(InterfaceUseCase, metaclass=ABCMeta):
    _errors = ErrorsUseCaseEnum

    async def _validate_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        if model is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=self._errors.NOT_FOUND.format(model=self._model_name),
            )
        return model


class BaseUseCaseValidAlreadyExists(InterfaceUseCase, metaclass=ABCMeta):
    _errors = ErrorsUseCaseEnum

    async def _validate_already_exists_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        if model is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=self._errors.ALREADY_REGISTERED.format(model=self._model_name),
            )


class BaseFilterModelUseCase(InterfaceUseCase, BaseUtilsUseCase, metaclass=ABCMeta):
    _get_first = False
    _errors = ErrorsUseCaseEnum

    async def filter(self):
        await self._validate_values_payload()
        models = await self._repository.filter(self._get_first, **self._payload_clean)
        if not models:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=self._errors.NOT_FOUND.format(model=self._model_name),
            )
        return models


class BaseHtmlRenderTemplate(metaclass=ABCMeta):
    _request: Request
    _templates = get_templates()
    _template_name: str

    async def _render_template_response(self, data: dict):
        context = {"request": self._request}
        context.update(data)
        return self._templates.TemplateResponse(self._template_name, context=context)
