FROM python:3

WORKDIR /usr/src/app

COPY src .

CMD [ "python", "main.py" ]