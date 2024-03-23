#!/bin/bash

# Name of the first container to check

sudo apt-get update
sudo apt install postgresql-client-common
sudo apt-get install postgresql-client -y
sudo snap install docker
sudo systemctl start snap.docker.dockerd.service

while ! sudo docker ps; do
    echo 'Waiting for docker to be ready'
    sudo snap install docker
    sudo systemctl start snap.docker.dockerd.service
    sleep 5
done

while ! sudo docker image ls | grep -wq ${BACKEND_IMAGE}; do
  sudo docker pull ${BACKEND_IMAGE}
  sleep 5
done

if sudo docker ps -a | grep -wq ${BACKEND_CONTAINER}; then
    echo "Stopping and removing ${BACKEND_CONTAINER}..."
    sudo docker stop ${BACKEND_CONTAINER}
    sudo docker rm ${BACKEND_CONTAINER}
fi

while ! sudo docker container ls | grep -wq ${BACKEND_CONTAINER}; do
  sudo docker run -d -p 5000:5000 --name ${BACKEND_CONTAINER} -e DB_USERNAME=${DB_USERNAME} -e DB_PASSWORD=${DB_PASSWORD} -e DB_NAME=${DB_NAME} -e DB_HOST=${DB_HOST} --platform=linux/amd64/v2 ${BACKEND_IMAGE}
  sleep 5
done

