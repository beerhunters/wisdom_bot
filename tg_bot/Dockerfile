# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в контейнер
#COPY requirements.txt .
# Копируем requirements.txt из родительской директории
COPY ../requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения в контейнер
COPY . /app/

# Переменная окружения для отключения буферизации вывода
ENV PYTHONUNBUFFERED=1
# Добавляем директорию tg_bot в PYTHONPATH
ENV PYTHONPATH=/app/tg_bot:$PYTHONPATH

# Указываем команду запуска приложения
CMD ["python", "/app/tg_bot/bot.py"]