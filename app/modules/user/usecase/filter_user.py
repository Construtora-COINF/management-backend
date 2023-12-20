from app.abstracts.usecase.base_usecase import BaseUseCaseValidDataBase
from app.abstracts.usecase.base_utils_usecase import BaseUtilsUseCase
from ..abstracts.base_user_usecase import BaseUserUseCase
from ..schema import FilterUserSchema


class FilterUserUseCase(BaseUserUseCase, BaseUtilsUseCase):
    _payload: FilterUserSchema

    def __init__(self, get_first: bool = False, **kwargs):
        super().__init__()
        self._payload = FilterUserSchema(**kwargs)
        self._get_first = get_first

    async def execute(self):
        await self._validate_values_payload()
        user = await self._repository.filter(self._get_first, **self._payload_clean)
        return await self._serializer(user)
