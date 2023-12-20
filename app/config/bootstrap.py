from fastapi import FastAPI

from app.config.settings import get_settings

setting = get_settings()


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=setting.APP_NAME,
        version=setting.APP_VERSION,
        description=setting.APP_DESCRIPTION,
        root_path=setting.ROOT_PATH,
    )

    return application
