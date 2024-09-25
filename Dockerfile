FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

COPY app /opt
COPY .env /opt
COPY requirements.txt /opt

RUN pip3 install --upgrade matplotlib
RUN pip3 install -r /opt/requirements.txt

EXPOSE 8000