# Use Python 3.9.6 as base image
FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN apk add --no-cache zlib-dev gcc musl-dev
RUN pip3 install -r requirements.txt