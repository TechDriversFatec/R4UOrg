#!/bin/sh
cd /home/ubuntu/

. cron/docker_prune.sh
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
