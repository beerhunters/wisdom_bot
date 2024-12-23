from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_wisdom = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Получить мудрость")]], resize_keyboard=True
)
