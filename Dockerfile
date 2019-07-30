FROM ubuntu:18.04
WORKDIR /xfinite

# intall cron & python
RUN apt-get update && apt-get install -y cron python python-pip

# copy program source
COPY ./src/ .

# install python dependencies
RUN ./start.sh

# copy cron source
COPY ./cron/ /etc/cron.d/

# set cron file permissions
RUN chmod 0644 /etc/cron.d/*

# apply cron job
RUN crontab /etc/cron.d/xfinite-cron

# run cron in foreground
CMD cron -f

# for debugging
#CMD /bin/bash