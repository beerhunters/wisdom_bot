# Wisdom Bot

**Wisdom Bot** is a Telegram bot that sends wisdom every day.  
The project uses PostgreSQL for data storage, Docker/Docker Compose for containerization, SQLAlchemy and Alembic for database handling, and NGinx for static.

---

## Technology Stack

- **Language**: Python  
- **Database**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Migrations**: Alembic  
- **Containerization**: Docker, Docker Compose  
- **Framework**: Django  
- **Static Server**: NGinx  

---

### Installation and configuration

### 1. Prepare the environment

- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).  
- Install PostgreSQL client (`psql`) to test the database.

---

### 2. Configuring the project

#### Create `docker-compose.yml`.
Follow these steps to bring up the container with PostgreSQL:  
1. clean up the Docker environment (optional):  
   ```bash
   docker system prune -a -f
   ```
2. Specify in ``docker-compose.yml``:  
   - PostgreSQL image.  
   - Login/password, database name, port, and hostname.  
3. Bring up the container:  
   ```bash
   docker-compose up --build
   ```
4. Check the database connection:  
   ```bash
   psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -p ${POSTGRES_PORT}
   ```

#### Creating a Dockerfile for Telegram bot
Create a `Dockerfile` by adding the working directory `/app`.

---

### 3. Working with a database

#### SQLAlchemy: creating a model
- Configure SQLAlchemy to interact with PostgreSQL.

#### Alembic: Migration Management
1. initialize Alembic:  
   ```bash.
   alembic init alembic
   ```
2. Customize ``alembic.ini``:  
   ```ini
   sqlalchemy.url = postgresql+psycopg2://<username>:<password>@localhost:<port>/<database>
   ```
   Or add the URL to `.env` to avoid changes to `alembic.ini`.
3. Make sure the connection in `env.py` is synchronous.

#### Creating and applying migrations
1. Create a migration:  
   ```bash
   alembic revision --autogenerate -m “Create tables”
   ```
2. Apply the migration:  
   ````bash
   alembic upgrade head
   ```

---

### 4. PostgreSQL container management

1. Connect to the container:  
   ```bash
   docker exec -it <container_id_or_name> psql -U <username> -d <database_name>
   ```
2. Get a list of all tables:  
   ```bash
   \dt
   ```

---

### 5. Configuring Ports

- PostgreSQL internal port: `5432`.  
- External access port: `5437`.

---

### 6. Django and NGinx

1. Project creation.  
   ```bash
   django-admin startproject admin_panel
   cd admin_panel
   ```
2. Configuring the connection to the database
   ```python
   DATABASES = {
       { “default”: {
           “ENGINE": ‘django.db.backends.postgresql’,
           “NAME": ‘your_database_name’,
           “USER": ‘your_database_user’,
           “PASSWORD": ‘your_database_password’,
           “HOST": ‘localhost’, # Specify the host of your container if you're working with Docker.
           “PORT": ”5432”
       }
   }
   ```
3. Creating a Django application
   ```bash
    python manage.py startapp core
   ```
4. Register the application in admin_panel/settings.py under INSTALLED_APPS
   ```python
    INSTALLED_APPS = [
    # Other standard applications
    { “core”,
   ]
   ```
5. Creating models for Django
   - Bring up the container with the database
   ```bash
    docker-compose up
   ```
   - Autogenerate models
   ```bash
    python manage.py inspectdb > core/models.py
   ```
6. Save the file and create migrations
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
7. Open the core/admin.py file and register the model.
   ```python
   from django.contrib import admin
   from .models import Product
   
   @admin.register(Product)
   Class ProductAdmin(admin.ModelAdmin):
       list_display = (“name”, “price”, “created_at”) # Fields displayed in the list
       search_fields = (“name”, “description”) # Fields to search for
   ```
8. Create a superuser to access the admin area
   ```bash
    python manage.py createsuperuser
   ```
9. Start the development server and open the admin panel, for testing purposes
   ```bash
    python manage.py runserver
   ```
10. In admin_panel/settings.py, add settings for static   
   ```python
    STATIC_URL = “/static/”
    STATIC_ROOT = BASE_DIR / “static”
   ```
   ```bash
    python manage.py collectstatic
   ```
11. dockerfile + docker-compose.yml

12. configure NGinx to handle static.

---

## Commands to run

1. **Build and start containers:**  
   ```bash
   docker-compose up --build
   ```
2. **Create tables and migrations:** ````  
   ```bash
   alembic revision --autogenerate -m “Create tables”
   alembic upgrade head
   ```
3. **Check database:**  
   ```bash
   psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -p ${POSTGRES_PORT}
   ```

---

## License

The project is distributed under the [MIT](https://github.com/beerhunters/wisdom_bot/blob/main/LICENSE.md) license.

---

## Contact

- Telegram: [Beerhunters](https://t.me/beerhunters)  
- GitHub: [Beerhunters](https://github.com/beerhunters/wisdom_bot)

Translated with www.DeepL.com/Translator (free version)
