## A "To Do" Application

You can add 'boards' and inside a board add some 'to do'.
Each 'to do' has a status that is done or not.

### Project structure:
```
.
├── .gitignore
├── requirements.txt
├── src
    ├── conf
    ├── boards
    └── manage.py

```

## Running application

Add database configuration in ("src/conf/local_settings.py") file.
Then change working directory to "src".
```
cd src

```
Then run the server.
```
python manage.py runserver

```

After the server is running, navigate to `http://localhost:8000` in your web browser:

Stop server using Ctrl + C in your terminal.      
