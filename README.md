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
   ```sql
   \dt
   ```

---

### 5. Настройка портов

- Внутренний порт PostgreSQL: `5432`.  
- Внешний порт для доступа: `5437`.

---

### 6. Django и NGinx

1. Подключите Django для управления серверной частью.  
2. Настройте NGinx для обработки статики.

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

Проект распространяется под лицензией [MIT](LICENSE).

---

## Контакты

- Telegram: [Ваш контакт](https://t.me/username)  
- GitHub: [Ваш репозиторий](https://github.com/username/wisdom_bot)
