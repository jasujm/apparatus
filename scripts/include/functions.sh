if [ "$(git rev-parse --show-toplevel)" != "$(pwd)" ]; then
    echo "This command must be run from the top level directory"
    exit 1
fi

server_name=${APPARATUS_SERVER_NAME}
nginx_conf_dir=${APPARATUS_NGINX_CONF_DIR:-./env/nginx}
secrets_dir=${APPARATUS_SECRETS_DIR:-./env/secrets}
