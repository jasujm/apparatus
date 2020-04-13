unset CDPATH

cd $(realpath $(dirname $0)/..)

server_name=${APPARATUS_SERVER_NAME}
nginx_conf_dir=${APPARATUS_NGINX_CONF_DIR:-./env/nginx}
secrets_dir=${APPARATUS_SECRETS_DIR:-./env/secrets}
