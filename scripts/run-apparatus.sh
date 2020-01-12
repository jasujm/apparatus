#!/bin/bash
if [ ! -f docker-compose.prod.yml ]; then
    echo 'Please ensure that the docker-compose files are present'
    exit 1;
fi
docker-compose -f docker-compose.yml -f docker-compose.certbot.yml -f docker-compose.prod.yml up -d --build
