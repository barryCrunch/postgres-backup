#build from ubntu 16.04
FROM ubuntu:16.04

#Update Software Repo
RUN apt-get update
RUN apt-get install python3 && python3-pip && postgresql-client

ADD . /
