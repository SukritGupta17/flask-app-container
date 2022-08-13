FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install python3 python3-pip

RUN pip install flask
COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run --host=0.0.0.0