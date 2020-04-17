#!/bin/bash

# Network

docker network create cassandra-net

# Cassandra nodes:

docker run -d --name cassandra-1 --network cassandra-net -p 9160:9160 -e "CASSANDRA_START_RPC=true" cassandra
docker run -d --name cassandra-2 --network cassandra-net -p 9161:9160 -e "CASSANDRA_START_RPC=true" -e CASSANDRA_SEEDS=cassandra-1 cassandra
docker run -d --name cassandra-3 --network cassandra-net -p 9162:9160 -e "CASSANDRA_START_RPC=true" -e CASSANDRA_SEEDS=cassandra-1 cassandra
docker run -d --name cassandra-4 --network cassandra-net -p 9163:9160 -e "CASSANDRA_START_RPC=true" -e CASSANDRA_SEEDS=cassandra-1 cassandra

# Note that cassandra-1 is, in this case, the cassandra seed.
# In a real-case infrastructure, for 4 nodes it is recommended to start the cluster with a single
# Cassandra seed, but then restart every node (starting from the Cassandra seed) with two nodes as
# seeds nodes.

# Check Cassandra cluster status:
docker exec -it cassandra-1 /bin/bash
nodetool status


# KairosDB nodes:
docker run -d --name kairos-1 --network cassandra-net -p 8080:8083 -p 4242:4242 -e "CASSANDRA_HOST_LIST=cassandra-1:9160,cassandra-2:9160,cassandra-3:9160,cassandra-4:9160" jimtonic/kairosdb
docker run -d --name kairos-2 --network cassandra-net -p 8081:8083 -p 4243:4242 -e "CASSANDRA_HOST_LIST=cassandra-1:9160,cassandra-2:9160,cassandra-3:9160,cassandra-4:9160" jimtonic/kairosdb
# "CASSANDRA_HOST_LIST=172.19.0.2:9160,172.19.0.3:9160,172.19.0.4:9160,172.19.0.5:9160"

# Nginx:
docker run -p 80:8080 --name nginx-app-kairosdb --network cassandra-net -v /path/to/nginx.conf:/etc/nginx/nginx.conf:ro nginx