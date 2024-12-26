# wisdom_bot
ТГ-бот с мудростями каждый день

1. Создание ТГ-бота
   - Процесс создания
2. Создание docker-compose.yml с поднятием БД на PostgreSQL
   - Удалить все
     - ❯ docker system prune -a -f
   - Выбор образа, который будет подыматься в Docker
   - Логин/пароль/название БД/порт/хост(имя сервиса из docker-compose.yml)
   - Поднять контейнер
     - ❯ docker-compose up --build
   - Проверить созданную БД - 
     - ❯ psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -p ${POSTGRES_PORT}
3. Создание Dockerfile для ТГ-бота
   - После создания папка проект /app
4. Создание модель в SQLAlchemy
   - Процесс создания
5. Создание таблиц через alembic
   5. 1. ❯ alembic init alembic
   5. 2. Файл alembic.ini 
      - sqlalchemy.url = postgresql+psycopg2://wisdom:wisdom@localhost:{port}/db
      - Если в .env добавить url для alembic, то можно не менять .ini файл
6. файл env.py, внимательно, что подключение к БД должно быть синхронным
   6. 1. См. файл
7. Запуск миграций
   7. 1. ❯ alembic revision --autogenerate -m "Create tables"
   7. 2. ❯ alembic upgrade head
8. Подключитесь к контейнеру с PostgreSQL, используя команду:
   - ❯ docker exec -it <container_id_or_name> psql -U <username> -d <database_name>
9. Список всех таблиц
   - \dt

7. Порты внутри контейнеров должны общаться по-внутреннему 5432, обращения извне по 5437
8. Добавление Django
9. Добавление статики через NGinx