FROM python:3.11.0a6-alpine3.15

WORKDIR /

COPY . /

RUN pip3 install -r requirements.txt

CMD [ "python3", "app/Server.py" ]