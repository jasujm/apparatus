#!/bin/bash

source scripts/include/functions.sh

mkdir -p $nginx_conf_dir ${secrets_dir}/{mysql,apparatus}

if [ ! $server_name ]; then
    read -p "Server name: " server_name
fi

read -p "Secret key: " -s apparatus_secret_key
read -p "MySQL user name: " -s mysql_user
read -p "MySQL password: " -s mysql_password

echo $mysql_password > ${secrets_dir}/mysql/mysql-apparatus-password
echo $mysql_user > ${secrets_dir}/mysql/mysql-apparatus-user

cat > ${secrets_dir}/apparatus/envfile <<EOF
SECRET_KEY=${apparatus_secret_key}
DATABASE_URL=mysql://${mysql_user}:${mysql_password}@mysql:3306/apparatus
EOF

echo "All done!

Add the following to your ~/.bashrc:

export APPARATUS_SERVER_NAME=${server_name}
export APPARATUS_SECRETS_DIR=$(realpath $secrets_dir)
export APPARATUS_NGINX_CONF_DIR=$(realpath $nginx_conf_dir)

Then source ~/.bashrc before proceeding"
