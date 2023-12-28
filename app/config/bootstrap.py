from fastapi import FastAPI
from loguru import logger

from app.config.settings import get_settings
import locale


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    setting = get_settings()
    application = FastAPI(
        title=setting.APP_NAME,
        version=setting.APP_VERSION,
        description=setting.APP_DESCRIPTION,
        root_path=setting.ROOT_PATH,
    )
    return application


def set_locale():
    try:
        locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
    except locale.Error as e:
        logger.error(e)
