from app.config.bootstrap import create_app
from app.config.db import close_connection_database, connect_to_database
from app.config.jwt import exception_jwt, init_jwt
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers
from app.config.static_files import init_static_files

app = create_app()
init_middlewares(app)
init_static_files(app)


@app.on_event("startup")
async def startup_db():
    await connect_to_database()


@app.on_event("startup")
async def startup_jwt():
    await init_jwt()


@app.on_event("startup")
async def startup_exception_jwt():
    await exception_jwt(app)


@app.on_event("startup")
async def startup_routers():
    await init_routers(app)


@app.on_event("shutdown")
async def shutdown_event():
    await close_connection_database()
