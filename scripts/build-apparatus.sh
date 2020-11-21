#!/bin/bash
#docker-compose build apparatus

if [ "$1" = "--push" ]; then
    docker push jasujm/apparatus
fi
