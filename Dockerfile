# syntax=docker/dockerfile:1
FROM python:latest

WORKDIR /sdn-projects

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY script.py ./

CMD [ "python", "./script.py"]

