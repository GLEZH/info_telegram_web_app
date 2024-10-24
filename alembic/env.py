import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from alembic import context

from info_telegram_web_app.app.models import Base
from info_telegram_web_app.config import DATABASE_URL

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = config.attributes.get('connection', None)
    if connectable is None:
        from sqlalchemy.ext.asyncio import create_async_engine
        connectable = create_async_engine(DATABASE_URL)

    async def do_run_migrations(connection: Connection):
        context.configure(connection=connection, target_metadata=target_metadata, literal_binds=True)

        async with context.begin_transaction():
            await context.run_migrations()

    asyncio.run(do_run_migrations(connectable))

run_migrations_online()
