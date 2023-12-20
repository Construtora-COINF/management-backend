from abc import ABCMeta

from fastapi import HTTPException, status
from fastapi_camelcase import CamelModel

from app.abstracts.database.base_repository import BaseRepository
from app.abstracts.usecase.enum import ErrorsUseCaseEnum
from app.interfaces.usecase_interface import InterfaceUseCase


class BaseUseCaseValidDataBase(InterfaceUseCase, metaclass=ABCMeta):
    def __init__(
        self, model_name: str, payload: CamelModel, repository: BaseRepository
    ):
        super().__init__(model_name, payload, repository)
        self._errors = ErrorsUseCaseEnum

    async def _validate_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        if model is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=self._errors.NOT_FOUND.format(model=self._model_name),
            )
        return model


class BaseUseCaseValidAlreadyExists(InterfaceUseCase, metaclass=ABCMeta):
    def __init__(
        self, model_name: str, payload: CamelModel, repository: BaseRepository
    ):
        super().__init__(model_name, payload, repository)
        self._errors = ErrorsUseCaseEnum

    async def _validate_already_exists_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        if model is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=self._errors.ALREADY_REGISTERED.format(model=self._model_name),
            )
