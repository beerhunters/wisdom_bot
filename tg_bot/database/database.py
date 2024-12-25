from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.ext.asyncio import async_sessionmaker
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = "postgresql+asyncpg://wisdom:wisdom@wisdom_db:5432/db"

# Создание асинхронного движка
engine = create_async_engine(
    DATABASE_URL, echo=True
)  # echo=True для логирования запросов

# Настройка сессионного фабрика
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# Асинхронный генератор для получения сессий
async def get_session():
    """
    Генератор асинхронных сессий для работы с базой данных.
    """
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise
        finally:
            await session.close()
