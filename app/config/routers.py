from fastapi import FastAPI
from fastapi_pagination import add_pagination
from loguru import logger


async def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.modules.core import helthcheck_router
    from app.modules.user import router as user_router
    from app.modules.notifications import router as notifications_router

    logger.info("Starting up routers...")
    app.include_router(helthcheck_router.router)
    app.include_router(user_router.router, prefix="/users", tags=["User"])
    app.include_router(
        notifications_router.router, prefix="/notifications", tags=["Notifications"]
    )
    add_pagination(app)
