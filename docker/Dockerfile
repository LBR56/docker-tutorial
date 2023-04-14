FROM python:3.9

LABEL version="v1.0.0"
LABEL description="python 도커 파일 만들기 연습"

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip

COPY sample.env /data/app/sample.env
ADD requirements.txt /data/app

WORKDIR /data/app

RUN pip install -r requirements.txt 

