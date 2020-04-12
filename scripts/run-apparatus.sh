#!/bin/bash
docker-compose -f docker-compose.yml -f docker-compose.certbot.yml up -d --build
