FROM python:2.7-alpine
RUN apt-get update && \
    apt-get -y install gcc g++ make libffi-dev openssl-dev
