# Wisdom Bot

**Wisdom Bot** — это Telegram-бот, отправляющий мудрости каждый день.  
Проект использует PostgreSQL для хранения данных, Docker/Docker Compose для контейнеризации, SQLAlchemy и Alembic для работы с базой данных, а также NGinx для статики.

---

## Стек технологий

- **Язык**: Python  
- **База данных**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Миграции**: Alembic  
- **Контейнеризация**: Docker, Docker Compose  
- **Фреймворк**: Django  
- **Сервер статики**: NGinx  

---

## Установка и настройка

### 1. Подготовка среды

- Установите [Docker](https://docs.docker.com/get-docker/) и [Docker Compose](https://docs.docker.com/compose/install/).  
- Установите PostgreSQL клиент (`psql`) для проверки базы данных.

---

### 2. Настройка проекта

#### Создание `docker-compose.yml`
Для поднятия контейнера с PostgreSQL выполните следующие шаги:  
1. Очистите Docker-среду (опционально):  
   ```bash
   docker system prune -a -f
   ```
2. Укажите в `docker-compose.yml`:  
   - Образ PostgreSQL.  
   - Логин/пароль, имя базы данных, порт и имя хоста.  
3. Поднимите контейнер:  
   ```bash
   docker-compose up --build
   ```
4. Проверьте подключение к базе данных:  
   ```bash
   psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -p ${POSTGRES_PORT}
   ```

#### Создание Dockerfile для Telegram-бота
Создайте `Dockerfile`, добавив рабочую директорию `/app`.

---

### 3. Работа с базой данных

#### SQLAlchemy: создание модели
- Настройте SQLAlchemy для взаимодействия с PostgreSQL.

#### Alembic: управление миграциями
1. Инициализация Alembic:  
   ```bash
   alembic init alembic
   ```
2. Настройте `alembic.ini`:  
   ```ini
   sqlalchemy.url = postgresql+psycopg2://<username>:<password>@localhost:<port>/<database>
   ```
   Или добавьте URL в `.env`, чтобы избежать изменений в `alembic.ini`.
3. Убедитесь, что подключение в `env.py` синхронное.

#### Создание и применение миграций
1. Создайте миграцию:  
   ```bash
   alembic revision --autogenerate -m "Create tables"
   ```
2. Примените миграцию:  
   ```bash
   alembic upgrade head
   ```

---

### 4. Управление контейнером PostgreSQL

1. Подключитесь к контейнеру:  
   ```bash
   docker exec -it <container_id_or_name> psql -U <username> -d <database_name>
   ```
2. Получите список всех таблиц:  
   ```bash
   \dt
   ```

---

### 5. Настройка портов

- Внутренний порт PostgreSQL: `5432`.  
- Внешний порт для доступа: `5437`.

---

### 6. Django и NGinx

1. Создание проекта.  
   ```bash
   django-admin startproject admin_panel
   cd admin_panel
   ```
2. Настройка подключение к БД
   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "your_database_name",
           "USER": "your_database_user",
           "PASSWORD": "your_database_password",
           "HOST": "localhost",  # Укажите хост вашего контейнера, если работаете с Docker
           "PORT": "5432",
       }
   }
   ```
3. Создание Django приложения
   ```bash
    python manage.py startapp core
   ```
4. Зарегистрируйте приложение в admin_panel/settings.py в разделе INSTALLED_APPS
   ```python
    INSTALLED_APPS = [
    # Другие стандартные приложения
    "core",
   ]
   ```
5. Создание моделей для Django
   - Поднять контейнер с БД
   ```bash
    docker-compose up
   ```
   - Автогенерация моделей
   ```bash
    python manage.py inspectdb > core/models.py
   ```
6. Сохраните файл и создайте миграции
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
7. Откройте файл core/admin.py и зарегистрируйте модель.
   ```python
   from django.contrib import admin
   from .models import Product
   
   @admin.register(Product)
   class ProductAdmin(admin.ModelAdmin):
       list_display = ("name", "price", "created_at")  # Поля, отображаемые в списке
       search_fields = ("name", "description")  # Поля для поиска
   ```
8. Создайте суперпользователя для доступа к админке
   ```bash
    python manage.py createsuperuser
   ```
9. Запустите сервер разработки и откройте админ-панель, для проверки
   ```bash
    python manage.py runserver
   ```
10. В admin_panel/settings.py добавьте настройки для статики   
   ```python
    STATIC_URL = "/static/"
    STATIC_ROOT = BASE_DIR / "static"
   ```
   ```bash
    python manage.py collectstatic
   ```
11. Dockerfile + docker-compose.yml

12. Настройте NGinx для обработки статики.

---

## Команды для запуска

1. **Сборка и запуск контейнеров:**  
   ```bash
   docker-compose up --build
   ```
2. **Создание таблиц и миграции:**  
   ```bash
   alembic revision --autogenerate -m "Create tables"
   alembic upgrade head
   ```
3. **Проверка базы данных:**  
   ```bash
   psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -p ${POSTGRES_PORT}
   ```

---

## Лицензия

Проект распространяется под лицензией [MIT](https://github.com/beerhunters/wisdom_bot/blob/main/LICENSE.md).

---

## Контакты

- Telegram: [Beerhunters](https://t.me/beerhunters)  
- GitHub: [Beerhunters](https://github.com/beerhunters/wisdom_bot)
