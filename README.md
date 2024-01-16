## A "To Do" Application

A RESTFul api wrote in Django framework.

You can add 'boards' and inside a board add some 'to do'.
Each 'to do' has a status that is done or not.

### Project structure:
```
.
├── .gitignore
├── web
    ├── conf
    ├── boards
    ├── manage.py
    ├── requirements.txt  
    └── Dockerfile

```

## Running application

Before go on production create local_settings.py file in [web/conf/](web/conf/) directory and add 'secret key' and 'allowed hosts' and 'database configuration' to it.

Then the models must be migrated.
```
docker run /usr/local/bin/python src/manage.py migrate
```

## DOCKER 

```
docker pull arian1200401050/todo
```

## API

To see a list of api URLs, visit the root domain of the host on which application is running.
