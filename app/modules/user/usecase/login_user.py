from fastapi import HTTPException, status
from fastapi_jwt_auth import AuthJWT
from passlib.hash import pbkdf2_sha256

from app.abstracts.usecase.base_usecase import BaseUseCaseValidDataBase
from app.modules.user import schema
from app.modules.user.abstracts.base_user_usecase import BaseUserUseCase
from app.modules.user.enum import UserMessagesEnum


class LoginUseCase(BaseUserUseCase, BaseUseCaseValidDataBase):
    _payload: schema.LoginUserSchema

    def __init__(self, payload: schema.LoginUserSchema, authorize: AuthJWT):
        super().__init__(payload)
        self._authorize = authorize

    async def _serializer_token(self, user):
        access_token = self._authorize.create_access_token(subject=user.email)
        return schema.JWTUserSchema(
            **dict(uuid=user.uuid, email=user.email, access_token=access_token)
        )

    async def execute(self):
        user = await self._validate_db(email=self._payload.email)
        if not pbkdf2_sha256.verify(self._payload.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=UserMessagesEnum.INVALID_PASSWORD,
            )
        return await self._serializer_token(user)
