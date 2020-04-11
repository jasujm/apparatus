#!/bin/bash
docker-compose exec certbot certbot certonly --webroot -w /var/www/certbot -d "$1" -d "www.$1"
docker-compose exec nginx /bin/bash -c "scripts/write-apparatus-conf.sh $1; nginx -s reload"
