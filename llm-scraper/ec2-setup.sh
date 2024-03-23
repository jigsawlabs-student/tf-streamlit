#!/bin/bash


# sudo apt-get update
# sudo apt install postgresql-client-common
# sudo apt-get install postgresql-client
# sudo snap install docker
# sudo systemctl start snap.docker.dockerd.service


export BACKEND_CONTAINER="backend"

export BACKEND_IMAGE="fill in"
export DB_USERNAME="postgres"
export DB_PASSWORD="password"
export DB_NAME="postgres"

while ! sudo docker image ls | grep -wq ${BACKEND_IMAGE}; do
  sudo docker pull ${BACKEND_IMAGE}
  sleep 5
done

if docker ps -a | grep -wq $BACKEND_CONTAINER; then
    echo "Stopping and removing $BACKEND_CONTAINER..."
    docker stop $BACKEND_CONTAINER
    docker rm $BACKEND_CONTAINER
fi

docker run -p 5000:5000 --name $BACKEND_CONTAINER -e DB_USERNAME=$DB_USERNAME -e DB_PASSWORD=$DB_PASSWORD -e DB_NAME=$DB_NAME -e DB_HOST=$DB_HOST $BACKEND_IMAGE
