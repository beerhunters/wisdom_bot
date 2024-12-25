FROM python:3.12.0-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache

# Копируем весь проект внутрь контейнера
COPY . .

# Указываем, что будем использовать Alembic
CMD ["alembic"]