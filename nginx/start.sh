#!/bin/bash
write-apparatus-conf.sh

trap 'kill $(jobs -p)' EXIT
while :; do
    sleep 1d
    nginx -s reload
done &
nginx -g 'daemon off;'
