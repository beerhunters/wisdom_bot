from sqlalchemy import (
    ForeignKey,
    String,
    BigInteger,
    func,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from sqlalchemy.ext.asyncio import AsyncAttrs


# Базовый класс для всех моделей
class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    """
    Модель пользователя.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String(20), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    # Связь с таблицей Wisdom
    wisdoms: Mapped[list["Wisdom"]] = relationship("Wisdom", back_populates="user")


class Wisdom(Base):
    """
    Модель мудрости.
    """

    __tablename__ = "wisdoms"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.tg_id"))
    message: Mapped[str] = mapped_column(String(128), nullable=True)
    author: Mapped[str] = mapped_column(String(128), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    # Связь с таблицей User
    user: Mapped[list["User"]] = relationship("User", back_populates="wisdoms")
