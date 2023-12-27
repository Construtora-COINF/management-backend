from abc import ABCMeta, abstractmethod

from fastapi_camelcase import CamelModel

from app.abstracts.database.base_repository import BaseRepository


class InterfaceUseCase(metaclass=ABCMeta):
    def __init__(
        self,
        model_name: str,
        payload: CamelModel,
        repository: BaseRepository,
    ):
        self._payload: CamelModel = payload
        self._repository: BaseRepository = repository
        self._model_name: str = model_name

    @abstractmethod
    async def execute(self):
        pass
