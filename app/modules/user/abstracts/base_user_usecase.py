from abc import ABC

from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.interfaces.usecase_interface import InterfaceUseCase
from app.modules.user import schema
from app.modules.user.model import User
from app.modules.user.repository import UserRepository


class BaseUserUseCase(InterfaceUseCase, ABC):
    _repository: UserRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("User", payload, UserRepository())
        self._pydantic_model = pydantic_model_creator(User)

    async def _serializer(self, model: User):
        pyd_model = await self._pydantic_model.from_tortoise_orm(model)
        return schema.GetUserSchema(**pyd_model.dict())
