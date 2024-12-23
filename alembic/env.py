# from logging.config import fileConfig
#
# from sqlalchemy import engine_from_config
# from sqlalchemy import pool
#
# from alembic import context
#
# from tg_bot.database.models import Base
#
# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config
#
# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)
#
# # add your model's MetaData object here
# # for 'autogenerate' support
# # from myapp import mymodel
# target_metadata = Base.metadata
# # target_metadata = None
#
# # other values from the config, defined by the needs of env.py,
# # can be acquired:
# # my_important_option = config.get_main_option("my_important_option")
# # ... etc.
#
#
# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode.
#
#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.
#
#     Calls to context.execute() here emit the given string to the
#     script output.
#
#     """
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )
#
#     with context.begin_transaction():
#         context.run_migrations()
#
#
# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode.
#
#     In this scenario we need to create an Engine
#     and associate a connection with the context.
#
#     """
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section, {}),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )
#
#     with connectable.connect() as connection:
#         context.configure(connection=connection, target_metadata=target_metadata)
#
#         with context.begin_transaction():
#             context.run_migrations()
#
#
# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()
# import asyncio
# from logging.config import fileConfig
#
# from sqlalchemy import pool
# from sqlalchemy.engine import Connection
# from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
#
# from alembic import context
# from tg_bot.database.models import Base
#
# # Настройка конфигурации Alembic.
# config = context.config
# fileConfig(config.config_file_name)
#
# # Указываем метаданные для моделей
# target_metadata = Base.metadata
#
# # Асинхронная строка подключения к базе данных
# DATABASE_URL = "postgresql+asyncpg://wisdom:wisdom@localhost:6432/wisdom"
#
#
# def run_migrations_offline() -> None:
#     """Запуск миграций в оффлайн-режиме."""
#     context.configure(
#         url=DATABASE_URL,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )
#
#     with context.begin_transaction():
#         context.run_migrations()
#
#
# async def run_migrations_online() -> None:
#     """Запуск миграций в онлайн-режиме."""
#     connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)
#
#     async with connectable.connect() as connection:
#         await connection.run_sync(
#             lambda conn: context.configure(
#                 connection=conn, target_metadata=target_metadata
#             )
#         )
#
#         with context.begin_transaction():
#             context.run_migrations()
#
#
# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     asyncio.run(run_migrations_online())
from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from alembic import context
from tg_bot.database.models import Base

# Настройка конфигурации Alembic.
config = context.config
fileConfig(config.config_file_name)

# Указываем метаданные для моделей
target_metadata = Base.metadata

# Синхронная строка подключения к базе данных
DATABASE_URL = "postgresql://wisdom:wisdom@localhost:6432/wisdom"


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        # literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # as_sql=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме."""
    # Используем синхронное подключение
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with engine.connect() as connection:
        # Передаем синхронное соединение в контекст Alembic
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # literal_binds=True,
            # as_sql=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
