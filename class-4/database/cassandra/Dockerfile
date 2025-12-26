# Use an official Cassandra image as a base image
FROM cassandra:latest
ENV CASSANDRA_CLUSTER_NAME=mycluster \
    CASSANDRA_SEEDS=seed1,seed2
COPY cassandra.yaml /etc/cassandra/cassandra.yaml
EXPOSE 7000 7001 7199 9042 9160
COPY ./cassandra-scripts/ /docker-entrypoint-initdb.d/
