#build from ubntu 16.04
FROM ubuntu:16.04
MAINTAINER Michael Barry "mbarry@packetdriving.com"
#Update Software Repo
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y postgresql-client-10
RUN apt-get install build-essential libssl-dev libffi-dev python3-dev
RUN pip3 install sh
RUN pip3 install azure

RUN mkdir /scripts
ADD backup.py /scripts

WORKDIR /scripts
