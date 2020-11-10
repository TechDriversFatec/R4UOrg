#!/bin/sh

sudo . /home/ubuntu/cron/docker_prune.sh

sudo docker stop $(docker ps -aq)

sudo docker rm $(docker ps -aq)

sudo docker rmi $(docker images -aq)

cd /home/ubuntu/r4u_application

sudo docker-compose -f docker-compose-migration.yml up -d

sudo docker-compose up -d

sudo robot --outputdir /home/ubuntu/robotLogs --nostatusrc robotTests.robot
