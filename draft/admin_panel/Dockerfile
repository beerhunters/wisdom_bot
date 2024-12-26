# Базовый образ
FROM python:3.12.0-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY django.requirements.txt /app/

# Установка Python-зависимостей
RUN pip install --upgrade pip && \
    pip install -r django.requirements.txt \
    && rm -rf /root/.cache

# Копирование всего проекта в контейнер
COPY . /app/

# Выполнение миграций, создание суперпользователя и запуск приложения
CMD python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" && \
    python manage.py collectstatic --no-input && \
    gunicorn admin_panel.wsgi:application --bind 0.0.0.0:8000 --log-level info