import re
import ssl
import aiohttp
from bs4 import BeautifulSoup
from aiohttp import ClientSession

from tg_bot.database.requests import add_wisdom
from tg_bot.logger import logger

# Ссылка на рандомный текст
WISDOM_URL = "https://randstuff.ru/saying/"


# Экранирование специальных символов
async def escape_markdown(text: str) -> str:
    """Экранирует специальные символы для MarkdownV2."""
    # Перечень символов, которые нужно экранировать
    special_chars = r"_*[]()~`>#+-=|{}.!"
    escape_pattern = re.compile(f"([{re.escape(special_chars)}])")
    return escape_pattern.sub(r"\\\1", text)


# Отключение проверки SSL
async def get_ssl():
    # Создание глобального SSL контекста
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context


# Получение случайной цитаты
async def fetch_wisdom(tg_id) -> str:
    """Получение мудрости с сайта."""
    try:
        async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
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

            wisdom = f"{quote}\n\nАвтор: {author}"

            await add_wisdom(tg_id, quote, author.split("—")[1])
        else:
            wisdom = "Не удалось найти мудрость на странице."

        # Экранирование текста для отправки
        clear_wisdom = await escape_markdown(wisdom)
        return clear_wisdom

    except aiohttp.ClientError as e:
        logger.error(f"Ошибка при запросе к {WISDOM_URL}: {e}")
        return "Не удалось получить мудрость. Попробуйте позже."
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        return "Произошла ошибка, попробуйте позже."
