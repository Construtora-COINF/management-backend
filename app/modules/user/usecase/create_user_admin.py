from passlib.hash import pbkdf2_sha256

from app.abstracts.usecase.base_usecase import BaseUseCaseValidAlreadyExists
from app.config.settings import get_settings
from app.modules.user.abstracts.base_user_usecase import BaseUserUseCase
from app.modules.user.schema import CreateUserSchema


class CreateUserAdminUseCase(BaseUserUseCase, BaseUseCaseValidAlreadyExists):
    __settings = get_settings()

    def __init__(self):
        super().__init__()
        self._create_admin_user = self.__settings.CREATE_ADMIN

    async def _validate(self):
        await self._validate_already_exists_db(email=self.__settings.EMAIL_ADMIN)
        if self._create_admin_user:
            return CreateUserSchema(
                email=self.__settings.EMAIL_ADMIN,
                name=self.__settings.NAME_ADMIN,
                password=pbkdf2_sha256.hash(self.__settings.PASSWORD_ADMIN),
                is_active=True,
            ).dict()
        return None

    async def execute(self):
        user_dict = await self._validate()
        if user_dict:
            await self._repository.create(user_dict)
