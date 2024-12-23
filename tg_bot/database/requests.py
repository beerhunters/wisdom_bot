from sqlalchemy import select

from tg_bot.database.database import async_session
from tg_bot.database.models import User


def connection(some_func):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await some_func(session, *args, **kwargs)

    return wrapper


@connection
async def add_user(session, tg_id, username, full_name):
    # Проверяем, существует ли уже пользователь с таким tg_id
    user = await session.scalar(select(User).where(User.tg_id == tg_id))

    if not user:
        # Если пользователь не существует, создаем новую запись
        new_user = User(
            tg_id=tg_id,
            username=username,
            full_name=full_name,
        )
        session.add(new_user)
        await session.commit()
        return new_user
