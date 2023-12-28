import logging
from functools import lru_cache
from typing import List

from decouple import config
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Setting(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="0.0.1")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="API")
    APP_NAME: str = config("APP_NAME", default="FastApi Boilerplate")
    APP_PORT: int = config("APP_PORT", default=8000, cast=int)
    ENVIRONMENT: str = config("ENVIRONMENT", default="local")
    ROOT_PATH: str = config("ROOT_PATH", default="/")
    TESTING: bool = config("TESTING", default=False, cast=bool)
    DB_URL = config("DB_URL")
    DB_TEST_URL = config("DB_TEST_URL")
    GENERATE_SCHEMAS = config("GENERATE_SCHEMAS")
    ALLOW_HEADERS: List = ["*"]
    ALLOW_METHODS: List = ["*"]
    ORIGINS: List = [
        "http://localhost",
        "http://localhost:8080",
    ]
    MODELS: List = [
        "aerich.models",
        "app.modules.user.model",
        "app.modules.notifications.model",
    ]
    # Adm user
    NAME_ADMIN: str = config("NAME_ADMIN")
    EMAIL_ADMIN: str = config("EMAIL_ADMIN")
    PASSWORD_ADMIN: str = config("PASSWORD_ADMIN")
    CREATE_ADMIN: bool = config("CREATE_ADMIN", default=False, cast=bool)

    # Amazon AWS
    AWS_ACCESS_KEY_ID: str = config("AWS_ACCESS_KEY_ID", cast=str)
    AWS_SECRET_ACCESS_KEY: str = config("AWS_SECRET_ACCESS_KEY", cast=str)
    AWS_REGION: str = config("AWS_REGION", default="sa-east-1", cast=str)

    # Coinf
    EMAIL_NO_REPLY: str = config(
        "EMAIL_NO_REPLY", default="no-reply@teste.com", cast=str
    )
    EMAIL_CONTACT: str = config("EMAIL_CONTACT", default="contact@teste.com", cast=str)


@lru_cache()
def get_settings():
    log.info("Loading Config Application.")
    return Setting()
