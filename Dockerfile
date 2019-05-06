#build from ubntu 16.04
FROM ubuntu:16.04
MAINTAINER Michael Barry "mbarry@packetdriving.com"
#Update Software Repo
RUN apt-get update && \
    apt-get install -y wget cron
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' >> /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y postgresql-client-10 && \
    apt-get install build-essential libssl-dev libffi-dev python3-dev
RUN pip3 install sh azure

RUN echo "update"
RUN mkdir /scripts
ADD backup.py /scripts
ADD restore.py /scripts

COPY cronjob /etc/cron.d/backup-task
RUN chmod 0644 /etc/cron.d/backup-task
RUN crontab /etc/cron.d/backup-task
RUN service cron start
CMD cron && tail -f /var/log/cron.log

WORKDIR /scripts
