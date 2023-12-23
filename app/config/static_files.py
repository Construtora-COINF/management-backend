from functools import lru_cache

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger


def init_static_files(app: FastAPI):
    logger.info("Starting static files...")
    app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@lru_cache()
def get_templates():
    return Jinja2Templates(directory="templates")
