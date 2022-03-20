FROM python:3.10.3-alpine3.15
WORKDIR /app

ENV FLASK_APP Server.py

ENV FLASK_RUN_HOST 0.0.0.0

ENV FLASK_DEBUG=1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "Server.py"]

