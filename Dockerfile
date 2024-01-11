FROM python:3.9.18-alpine3.19

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/manage.py", "migrate"]
