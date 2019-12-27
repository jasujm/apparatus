#!/bin/bash
docker exec -it apparatus_certbot_1 certbot certonly --webroot -w /var/www/certbot -d "$1" -d "www.$1"
docker exec apparatus_nginx_1 /bin/bash -c '/usr/bin/write-apparatus-conf.sh; nginx -s reload'
