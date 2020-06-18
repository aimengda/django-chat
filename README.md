# django-chat
___
small real time chat app based on Django

## Setup
___
### Python Setup
Install python 3.8.3( don't forget to add python to PATH), after installation, open your cmd and run the following command in the folder you want the virtual environment in.

    python -m venv your_venv_name

activate your virtual environment and switch to the project folder, then run:

    pip install -r requirements.txt

**Don't close the terminal because we will use it later.**
###  Database Setup
Download and install postgre sql 11. Then login to the PgAdmin page to create a new user for the APP, please make sure that this user have full contorl to the database. Then open settings.py and edit database settings:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'databasename', # your database name
            'USER': 'username', # the username of the user you just created
            'PASSWORD': 'password', # the username of the user you just created
            'HOST': 'host', # for local database, it should be "localhost" or 127.0.0.1
            'PORT':'port' # the port your database listen in
        }
    }

*Alternatively, you can use other databases(MySQl, Orcale, MariaDB, SQLite), please refer to [django document](https://docs.djangoproject.com/en/3.0/ref/databases/) for the setup.
For other databases such as Microsoft SQL, please search the internet to get the right configuration.*

After that, please go to the terminal and run below command to create table(related to default django admin) in the database:

    python manage.py makemigrations
    python manage.py migrate

### launch
When all the setup completed, just run below command to launch the webserver.

    python manage.py runserver

Then you can see the webpage on http://127.0.0.1:8000