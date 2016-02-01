FROM ubuntu:latest
MAINTAINER Dmitri Melnikov
EXPOSE 8080

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /shortly
WORKDIR /shortly
RUN pip install -r requirements.txt

CMD ["gunicorn.sh"]
