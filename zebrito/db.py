import contextlib
import asyncpg
from zebrito.settings import settings

async def get_pool():
    return await asyncpg.create_pool(
        dsn=settings.db_url,
    )

@contextlib.asynccontextmanager
async def get_db_connection_pool(app):
    app.state.db_pool = await get_pool()
    yield
    await app.state.db_pool.close()