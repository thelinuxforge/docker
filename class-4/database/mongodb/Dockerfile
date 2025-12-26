# Use an official MongoDB image as a base image
FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME=admin \
    MONGO_INITDB_ROOT_PASSWORD=adminpassword \
    MONGO_INITDB_DATABASE=mydatabase
COPY mongod.conf /etc/mongod.conf
EXPOSE 27017
CMD ["mongod", "--config", "/etc/mongod.conf"]
