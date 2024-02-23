from fastapi import FastAPI
from zebrito.settings import settings
from zebrito.db import get_db_connection_pool
from zebrito.views import router

app = FastAPI(
    title=settings.APP_TITLE,
    lifespan=get_db_connection_pool)


app.include_router(router)