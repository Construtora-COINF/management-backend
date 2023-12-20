from passlib.hash import pbkdf2_sha256

from app.abstracts.usecase.base_usecase import BaseUseCaseValidAlreadyExists
from app.config.settings import get_settings
from app.modules.user.abstracts.base_user_usecase import BaseUserUseCase
from app.modules.user.schema import PostUserSchema

settings = get_settings()


class CreateUserAdminUseCase(BaseUserUseCase, BaseUseCaseValidAlreadyExists):
    def __init__(self):
        super().__init__()
        self._create_admin_user = settings.CREATE_ADMIN

    async def _validate(self):
        await self._validate_already_exists_db(email=settings.EMAIL_ADMIN)
        if self._create_admin_user:
            return PostUserSchema(
                email=settings.EMAIL_ADMIN,
                name=settings.NAME_ADMIN,
                password=pbkdf2_sha256.hash(settings.PASSWORD_ADMIN),
                is_active=True,
            ).dict()
        return None

    async def execute(self):
        user_dict = await self._validate()
        if user_dict:
            await self._repository.create(user_dict)
