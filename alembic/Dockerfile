FROM python:3.12-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект (для миграций)
COPY . /app/

# Точка входа по умолчанию для Alembic
#ENTRYPOINT ["alembic"]