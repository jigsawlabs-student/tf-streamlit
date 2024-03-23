#!/bin/bash


# sudo apt-get update
# sudo apt install postgresql-client-common
# sudo apt-get install postgresql-client
# sudo snap install docker
# sudo systemctl start snap.docker.dockerd.service

export NETWORK_NAME="jobs-scraper"
export BACKEND_CONTAINER="backend"
export FRONTEND_CONTAINER="frontend"
export BACKEND_IMAGE="jek2141/scraper_backend"
export FRONTEND_IMAGE="jek2141/scraper_frontend"
export DB_USERNAME="postgres"
export DB_PASSWORD="password"
export DB_NAME="postgres"

while ! sudo docker image ls | grep -wq ${BACKEND_IMAGE}; do
  sudo docker pull ${BACKEND_IMAGE}
  sleep 5
done

docker pull $FRONTEND_IMAGE

if docker ps -a | grep -wq $BACKEND_CONTAINER; then
    echo "Stopping and removing $BACKEND_CONTAINER..."
    docker stop $BACKEND_CONTAINER
    docker rm $BACKEND_CONTAINER
fi

if docker ps -a | grep -wq $FRONTEND_CONTAINER; then
    echo "Stopping and removing $FRONTEND_CONTAINER..."
    docker stop $FRONTEND_CONTAINER
    docker rm $FRONTEND_CONTAINER
fi

if ! docker network ls | grep -q $NETWORK_NAME; then
  echo "Network $NETWORK_NAME does not exist. Creating..."
  docker network create $NETWORK_NAME
else
  echo "Network $NETWORK_NAME already exists, skipping."
fi



docker run -d -p 5000:5000 --network $NETWORK_NAME --name $BACKEND_CONTAINER -e DB_USERNAME=$DB_USERNAME -e DB_PASSWORD=$DB_PASSWORD -e DB_NAME=$DB_NAME -e DB_HOST=$DB_HOST --platform=linux/amd64/v2 $BACKEND_IMAGE
docker run -d -p 80:80 --network $NETWORK_NAME --name $FRONTEND_CONTAINER --platform=linux/amd64/v2 $FRONTEND_IMAGE