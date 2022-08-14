FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install python3 python3-pip

COPY . /opt/source-code
WORKDIR /opt/source-code

RUN pip install --no-cache-dir -r requirements.txt


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app