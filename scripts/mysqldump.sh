#!/bin/bash

source $(dirname $0)/include/functions.sh

docker-compose exec -T mysql mysqldump -u$(< $APPARATUS_SECRETS_DIR/mysql/mysql-apparatus-user) -p$(< $APPARATUS_SECRETS_DIR/mysql/mysql-apparatus-password) --all-databases
