#!/bin/bash

#Stopping containers

docker stop kairosdb-1 kairosdb-2

docker stop cassandra-1 cassandra-2 cassandra-3 cassandra-4


# Remove all docker containers that are stopped
docker container rm $(docker container ls -aq)

#Removing containers (one at a time)
docker rm kairosdb-1 kairosdb-22

docker rm cassandra-1 cassandra-2 cassandra-3 cassandra-4

#Removing network
docker network rm cassandra-net