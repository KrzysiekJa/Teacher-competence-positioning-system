# syntax=docker/dockerfile:1
FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev
RUN pip install -r requirements.txt
COPY . /code/