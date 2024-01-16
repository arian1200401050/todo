## A "To Do" Application

A RESTFul api wrote in Django framework.

You can add 'boards' and inside a board add some 'to do'.
Each 'to do' has a status that is done or not.

### Project structure:
```
.
├── .gitignore
├── Dockerfile
├── requirements.txt
├── src
    ├── conf
    ├── boards
    └── manage.py

```

## Running application

Before go on production create local_settings.py file in [src/conf/](src/conf/) directory and add 'secret key' and 'allowed hosts' and 'database configuration' to it.

Then the models must be migrated.
```
docker run /usr/local/bin/python src/manage.py migrate
```

## API

To see a list of api URLs, visit the root domain of the host on which application is running.

## DOCKER 
[https://hub.docker.com/repository/docker/arian1200401050/todo/general](https://hub.docker.com/repository/docker/arian1200401050/todo/general)
