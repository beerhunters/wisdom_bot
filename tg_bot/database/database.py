from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")
port = os.getenv("DB_PORT")

# Получение URL базы данных из переменных окружения
DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@localhost:{port}/{database}"

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
