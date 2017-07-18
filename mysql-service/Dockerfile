FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE test
ENV MYSQL_USER root
ENV MYSQL_PASSWORD root

RUN apt-get update && apt-get install -y vim


ADD rolloutScriptMOMv1.4.sql /docker-entrypoint-initdb.d
