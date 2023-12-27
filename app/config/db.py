from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise
from tortoise.contrib.starlette import register_tortoise

from .settings import get_settings


def get_tortoise_config():
    settings = get_settings()
    return {
        "connections": {"default": settings.DB_URL},
        "apps": {
            "models": {
                "models": settings.MODELS,
                "default_connection": "default",
            },
        },
    }


def init_db(app: FastAPI):
    """This function is to configuration database credentials"""
    settings = get_settings()
    register_tortoise(
        app=app,
        db_url=settings.DB_URL if not settings.TESTING else settings.DB_TEST_URL,
        generate_schemas=settings.GENERATE_SCHEMAS,
        modules={"models": settings.MODELS},
    )


async def connect_to_database() -> None:
    logger.info("Starting up database Tortoise ORM... ")
    settings = get_settings()
    await Tortoise.init(
        db_url=settings.DB_URL,
        modules={"models": settings.MODELS},
    )


async def close_connection_database() -> None:
    logger.info("Shutting down, closing Tortoise connections...")
    await Tortoise.close_connections()


""" This config is for generate migrations.bkp by aerich """
TORTOISE_ORM = get_tortoise_config()
