FROM alpine

RUN which crond && \
    rm -rf /etc/periodic

RUN apk add curl

RUN mkdir /code
WORKDIR /code

ADD ./crontab/ /code/

ENTRYPOINT ["/code/entrypoint.sh"]

# source: `docker run --rm -it alpine  crond -h`
# -f | Foreground
# -l N | Set log level. Most verbose 0, default 8
CMD ["crond", "-f", "-l", "2"]
