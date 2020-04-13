#!/bin/bash

source scripts/include/functions.sh

if [ ! $server_name ]; then
    echo "APPARATUS_SERVER_NAME not set"
    exit 1
fi

docker-compose exec certbot certbot certonly --webroot -w /var/www/certbot -d "${server_name}" -d "www.${server_name}"
scripts/write-nginx-conf.sh tls > ${nginx_conf_dir}/default.conf
docker-compose exec nginx /bin/bash -c "nginx -s reload"
