from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from database.requests import add_user
from keyboards.basic import get_wisdom
from logger import logger
from utils import fetch_wisdom


# Инициализация роутера
user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик команды /start."""
    tg_id = message.from_user.id
    username = message.from_user.username or f"user_{tg_id}"
    full_name = message.from_user.full_name or "Неизвестный пользователь"
    try:
        await add_user(tg_id, username, full_name)
    except Exception as e:
        logger.error(f"Ошибка записи в БД: {e}")
    await message.answer(
        "Привет! Нажмите кнопку ниже, чтобы получить мудрость.",
        reply_markup=get_wisdom,
    )


@user.message(F.text == "Получить мудрость")
async def wisdom_handler(message: Message):
    """Обработчик кнопки 'Получить мудрость'."""
    wisdom = await fetch_wisdom()
    await message.answer(f"||{wisdom}||", parse_mode=ParseMode.MARKDOWN_V2)
