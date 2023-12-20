from ..abstracts.base_user_usecase import BaseUserUseCase


class GetAllUserUseCase(BaseUserUseCase):
    def __init__(self):
        super().__init__()

    async def execute(self):
        users = await self._repository.get_all()
        return [await self._serializer(user) for user in users]
