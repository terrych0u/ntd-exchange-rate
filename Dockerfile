FROM python:3.7.2-alpine3.8
MAINTAINER terry chou <tequilas721@gmail.com>

ARG SLACK_CHANNEL_ID
ENV SLACK_CHANNEL_ID_ENV=$SLACK_CHANNEL_ID

ARG SLACK_CHANNEL_NAME
ENV SLACK_CHANNEL_NAME_ENV=$SLACK_CHANNEL_NAME

ARG CURRENCY_TYPE
ENV CURRENCY_TYPE_ENV=$CURRENCY_TYPE


COPY requirements.txt /tmp/requirements.txt
COPY beautifulsoup.py /usr/local/bin/beautifulsoup.py

RUN apk add --no-cache g++ libxml2-dev libxslt-dev && pip install --no-cache-dir -r /tmp/requirements.txt

ENTRYPOINT ["/usr/local/bin/beautifulsoup.py"]
