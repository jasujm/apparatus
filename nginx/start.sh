#!/bin/bash
echo "server_name .${SERVER_NAME} localhost 127.0.0.1;" > /etc/nginx/conf.d/include/server_name.conf
write-apparatus-conf.sh

while :; do
    sleep 1d
    nginx -s reload
done &
nginx -g 'daemon off;'
