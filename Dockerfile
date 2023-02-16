FROM python:3.10.3-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . .

COPY ./entrypoint.sh .
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]