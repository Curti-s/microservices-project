FROM postgres:alpine

# extend postgres image by adding a SQL file to the
# docker-entrypoint-initdb.d directory, which will execute
# on init
ADD create.sql /docker-entrypoint-initdb.d