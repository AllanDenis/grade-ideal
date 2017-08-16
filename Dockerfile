FROM ubuntu:latest
MAINTAINER Allan Denis "allancomll@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install -U pip flask
COPY . /app
WORKDIR ./app
RUN pip3 install -r requirements.txt
RUN python3 --version
ENTRYPOINT ["python3"]
CMD ["api_flask.py"]

