from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.abstracts.usecase.base_usecase import BaseUseCaseValidAlreadyExists
from app.modules.user import schema
from app.modules.user.abstracts.base_user_usecase import BaseUserUseCase


class CreateUserUseCase(BaseUserUseCase, BaseUseCaseValidAlreadyExists):
    def __init__(self, payload: schema.CreateUserSchema):
        super().__init__(payload)
        self._payload = payload

    async def execute(self):
        await self._validate_already_exists_db(email=self._payload.email)
        self._payload.password = pbkdf2_sha256.hash(self._payload.password)
        user = await self._repository.create(self._payload.dict())
        return await self._serializer(user)
