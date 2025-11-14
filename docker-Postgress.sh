#!/bin/bash 

echo "Pulling docker postgress image"

docker pull postgres:latest

echo "safe run"

docker run -d \
  --name future_sales_db \
  -e POSTGRES_USER=mandla \
  -e POSTGRES_PASSWORD=secret123 \
  -e POSTGRES_DB=future_sales \
  -p 5432:5432 \
  postgres:latest




echo "check running container"
docker ps 


docker image ls 


