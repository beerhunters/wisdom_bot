import aiohttp
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from bs4 import BeautifulSoup
import ssl
from tg_bot.keyboards.basic import keyboard
from tg_bot.logger import logger

# URL для получения мудрости
WISDOM_URL = "https://randstuff.ru/saying/"

# Создание глобального SSL контекста
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Инициализация роутера
user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик команды /start."""
    await message.answer(
        "Привет! Нажмите кнопку ниже, чтобы получить мудрость.",
        reply_markup=keyboard,
    )


@user.message(F.text == "Получить мудрость")
async def wisdom_handler(message: Message):
    """Обработчик кнопки 'Получить мудрость'."""
    try:
        # Запрос к сайту
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=ssl_context)
        ) as session:
            async with session.get(WISDOM_URL) as response:
                response.raise_for_status()
                page_content = await response.text()

        # Парсинг страницы
        soup = BeautifulSoup(page_content, "html.parser")
        saying_div = soup.find("div", {"id": "saying"})

        if saying_div:
            quote_td = saying_div.find("td")
            author_span = saying_div.find("span", {"class": "author"})

            quote = (
                quote_td.text.strip().split("—")[0]
                if quote_td
                else "Не удалось получить цитату."
            )
            author = author_span.text.strip() if author_span else "Автор неизвестен"

            wisdom = f"{quote}\n\nАвтор {author}"
        else:
            wisdom = "Не удалось найти мудрость на странице."

        await message.answer(wisdom)

    except aiohttp.ClientError as e:
        logger.error(f"Ошибка при запросе к {WISDOM_URL}: {e}")
        await message.answer("Не удалось получить мудрость. Попробуйте позже.")
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        await message.answer("Произошла ошибка, попробуйте позже.")
