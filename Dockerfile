FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv python3-dev libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/app

WORKDIR /opt/app

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY app /opt/app/
COPY .env /opt/app/
COPY requirements.txt /opt/app/

RUN pip3 install --no-cache-dir -r /opt/app/requirements.txt

EXPOSE 8000

CMD ["python3", "main.py"]