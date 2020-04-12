#!/bin/bash

if [ "$(git rev-parse --show-toplevel)" != "$(pwd)" ]; then
    echo "This command must be run from the top level directory"
    exit 1
fi

server_name=${APPARATUS_SERVER_NAME}
nginx_conf_dir=${APPARATUS_NGINX_CONF_DIR}

if [ ! $server_name ]; then
    echo "APPARATUS_SERVER_NAME not set"
    exit 1
fi

if [ ! $nginx_conf_dir ]; then
    echo "APPARATUS_NGINX_CONF_DIR not set"
    exit 1
fi

docker-compose -f docker-compose.yml -f docker-compose.certbot.yml exec certbot certbot certonly --webroot -w /var/www/certbot -d "${server_name}" -d "www.${server_name}"
scripts/write-nginx-conf.sh tls > ${nginx_conf_dir}/default.conf
docker-compose -f docker-compose.yml -f docker-compose.certbot.yml exec nginx /bin/bash -c "nginx -s reload"
