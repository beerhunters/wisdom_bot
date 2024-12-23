from logging.config import fileConfig

from sqlalchemy import create_engine, pool

from alembic import context
from tg_bot.database.models import Base

# Настройка конфигурации Alembic.
config = context.config
fileConfig(config.config_file_name)

# Указываем метаданные для моделей
target_metadata = Base.metadata

# Синхронная строка подключения к базе данных
DATABASE_URL = "postgresql://wisdom:wisdom@wisdom-db:5432/wisdom"


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
