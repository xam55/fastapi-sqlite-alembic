from contextlib import asynccontextmanager
from pathlib import Path

from alembic import command
from alembic.config import Config
from fastapi import FastAPI

from core.database import engine
from routers import router


def run_upgrade(connection) -> None:
    alembic_cfg = Config(str(Path(__file__).with_name("alembic.ini")))
    alembic_cfg.attributes["connection"] = connection
    command.upgrade(alembic_cfg, "head")


async def run_pending_migrations() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(run_upgrade)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await run_pending_migrations()
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(router)