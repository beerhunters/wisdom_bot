import os
import logging
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import create_engine, pool
from alembic import context
from tg_bot.database.models import Base

# Настройка конфигурации Alembic.
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger(__name__)

# Метаданные для моделей
target_metadata = Base.metadata

# Загружаем переменные окружения
load_dotenv()

# Получаем параметры базы данных
# try:
#     user = os.getenv("POSTGRES_USER")
#     password = os.getenv("POSTGRES_PASSWORD")
#     host = "localhost"
#     # host = "wisdom"  # Название сервиса в docker-compose
#     database = os.getenv("POSTGRES_DB")
#     port = os.getenv("POSTGRES_PORT")
#     DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
# except KeyError as e:
#     raise RuntimeError(f"Missing environment variable: {e}")

DATABASE_URL = os.getenv("DB_URL_ALEMBIC")


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме."""
    logger.info("Running migrations in offline mode...")
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме."""
    logger.info("Running migrations in online mode...")
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with engine.connect() as connection:
        try:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
            )
            with context.begin_transaction():
                context.run_migrations()
        except Exception as e:
            logger.error(f"Error during migration: {e}")
            raise


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
