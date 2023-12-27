from app.abstracts.usecase.base_usecase import (
    BaseFilterModelUseCase,
)
from ..abstracts.base_user_usecase import BaseUserUseCase
from ..schema import FilterUserSchema


class FilterUserUseCase(BaseUserUseCase, BaseFilterModelUseCase):
    _payload: FilterUserSchema

    def __init__(self, get_first: bool = False, **kwargs):
        super().__init__(payload=FilterUserSchema(**kwargs))
        self._get_first = get_first

    async def execute(self):
        users = await self.filter()
        if self._get_first:
            return await self._serializer(users)
        return [await self._serializer(flavor) for flavor in users]
