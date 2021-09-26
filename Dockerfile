FROM python:3.10.0rc2-slim-buster
ENV PYTHONUNBUFFERED = 1
WORKDIR /meeting_room

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
