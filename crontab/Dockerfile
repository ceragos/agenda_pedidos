FROM centos:centos7

RUN yum install -y cronie curl && \
    rm -rf /etc/cron.*/*

RUN mkdir /code
WORKDIR /code

COPY . .

ENTRYPOINT ["/entrypoint.sh"]
# https://www.unix.com/man-page/centos/8/cron/
# -n| Tells  the  daemon  to run in the foreground.  This can be useful when starting it out of init. With this option is needed to change pam setting.  /etc/pam.d/crond must not enable pam_loginuid.so module.
CMD ["crond", "-n"]
