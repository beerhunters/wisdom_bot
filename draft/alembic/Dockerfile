FROM python:3.12.0-slim

WORKDIR /app

# Установка зависимостей
COPY alembic.requirements.txt /app/

RUN pip install --no-cache-dir -r alembic.requirements.txt \
    && rm -rf /root/.cache

# Копируем весь проект внутрь контейнера
COPY . /app/

# Указываем, что будем использовать Alembic
CMD ["alembic"]