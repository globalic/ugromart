FROM python:3.7.10-slim-stretch

LABEL maintainer="eleazar.yewa.harold@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

