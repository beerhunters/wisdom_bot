import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
from dotenv import load_dotenv

from tg_bot.logger import logger


from handlers import user


async def main():
    """Главная функция для запуска бота."""
    load_dotenv()
    bot = Bot(
        token=os.getenv("BOT_TOKEN"),
        # default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
    )
    dp = Dispatcher()

    # Регистрация обработчиков
    dp.include_router(user)
    bot_commands = [BotCommand(command="/start", description="Перезапустить бота")]
    await bot.set_my_commands(bot_commands)
    # Запуск бота
    try:
        logger.info("Бот запущен...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при работе бота: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
