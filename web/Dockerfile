FROM python:3.9.18-alpine3.19

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "/usr/local/bin/gunicorn", "conf.wsgi", "-w 2", "-b :8000" ]
