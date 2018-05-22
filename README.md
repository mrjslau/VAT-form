# Python VAT forms

\#5 task for Python course with Django framework

## Prerequisites
1. Create and use virtual environment for this project
```
$ virtualenv *name*
$ source *path_to_env*/bin/activate
```

2. Install neccessary packages to the environment
```
$ pip install django pillow psycopg2 psycopg2-binary
```

3. Fill local_settings.py.temp with DATABASE details and save without ".temp"

## Running
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```