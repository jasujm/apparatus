#!/bin/bash

source scripts/include/functions.sh

if [ ! $server_name ]; then
    echo "APPARATUS_SERVER_NAME not set"
    exit 1
fi

if docker-compose run -T --rm nginx test -d /etc/letsencrypt/live/${server_name}; then
    echo "TLS certificate found"
    write_nginx_config_arg=tls
else
    echo "TLS certificate not found. Please run scripts/get-certs.sh."
    write_nginx_config_arg=
fi

scripts/write-nginx-conf.sh $write_nginx_config_arg > ${nginx_conf_dir}/default.conf

docker-compose build --pull
docker-compose up -d
docker-compose exec nginx /bin/bash -c "nginx -s reload"
