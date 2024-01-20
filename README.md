## A "To Do" Application

A RESTFul api wrote in Django framework.

You can add 'boards' and inside a board add some 'to do'.
Each 'to do' has a status that is done or not.

### Project structure:
```
.
├── nginx
    ├── Dockerfile
    └── nginx.conf
├── web
    ├── boards
       ├── models.py
       ├── serializers.py
       ├── tests.py
       ├── urls.py
       └── views.py
    ├── conf
       ├── settings_development.py
       ├── settings_production.py
       ├── settings.py
       ├── urls.py
       └── wsgi.py
    ├── Dockerfile
    ├── manage.py
    └── requirements.txt  
├── .gitignore
├── docker-compose.yml
└── production.yml

```

## Running application

First of all clone the project using git.

```
git clone https://github.com/arian1200401050/todo
```

Then change the working directory to root of project. 

```
cd todo
```

Then before go on procution, create the .env file at the directory level of production.yml file and set the IS_PRODUCTION=1 and set the SECRET_KEY, DB_NAME, DB_HOST, DB_USER and DB_PASSWORD in it.

Then run multi-container application using docker compose.

```
docker compose -f production.yml up --build -d
```

Then collect the static files to serve with nginx instead gunicorn server to make the app load faster.

```
docker compose -f production.yml exec web /usr/local/bin/python manage.py collectstatic
```

Then the last thing before we can use the app is that the models need to be migrated.

```
docker compose -f production.yml exec web /usr/local/bin/python manage.py migrate
```

## API

To see a list of api URLs, visit the root domain of the host on which application is running.
