FROM python:3.9.18-alpine3.19

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "/usr/local/bin/python", "manage.py",  "runserver", "0.0.0.0:8000" ]