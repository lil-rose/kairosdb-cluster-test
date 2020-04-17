#!/bin/bash

#Stopping containers

docker stop kairos-1 kairos-2

docker stop cassandra-1 cassandra-2 cassandra-3 cassandra-4


# Remove all docker containers that are stopped
docker container rm $(docker container ls -aq)

#Removing containers (one at a time)
docker rm kairos-1 kairos-2

docker rm cassandra-1 cassandra-2 cassandra-3 cassandra-4

#Removing network
docker network rm cassandra-net