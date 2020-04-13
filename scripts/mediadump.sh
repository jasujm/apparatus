#!/bin/bash

source $(dirname $0)/include/functions.sh

docker-compose exec -T apparatus tar --to-stdout -C /var/www/apparatus -cp media
