# syntax=docker/dockerfile

FROM ubuntu:latest
# Install cron
RUN apt-get update && apt-get -y install cron && apt-get -y install pip
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./. /usr/app/
RUN pip install -r requirements.txt
EXPOSE 8000:8000