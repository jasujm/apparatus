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
