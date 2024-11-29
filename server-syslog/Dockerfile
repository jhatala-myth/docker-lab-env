FROM alpine:latest
RUN apk add --no-cache rsyslog logrotate tzdata
EXPOSE 514/tcp 514/udp
RUN mkdir -p /etc/rsyslog.d
CMD ["rsyslogd", "-n"]
