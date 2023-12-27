from abc import ABC
from fastapi_camelcase import CamelModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.interfaces.usecase_interface import InterfaceUseCase
from app.modules.notifications.model import Notification
from app.modules.notifications.repository import NotificationRepository
from app.modules.notifications import schema


class BaseNotificationUseCase(InterfaceUseCase, ABC):
    _repository: NotificationRepository

    def __init__(self, payload: CamelModel = None):
        super().__init__("Notification", payload, NotificationRepository())
        self._pydantic_model = pydantic_model_creator(Notification)

    async def _serializer(self, model: Notification):
        pyd_model = await self._pydantic_model.from_tortoise_orm(model)
        return schema.GetNotificationSchema(**pyd_model.dict())
