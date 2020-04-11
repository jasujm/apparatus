#!/bin/bash

server_name=${APPARATUS_SERVER_NAME}

if [ ! $server_name ]; then
    echo "APPARATUS_SERVER_NAME not set"
    exit 1
fi

cat <<EOF
server {
    listen       [::]:80 default_server;
    listen       80 default_server;
    return       444;
}

server {
    listen       [::]:80;
    listen       80;
    server_name  .${server_name} localhost 127.0.0.1;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return       301 https://\$host\$request_uri;
    }
}
EOF

# Only enable the HTTPS server serving the apparatus app if TLS certs
# are found. This allows first exposing ACME endpoints via HTTP, and
# then running the main website with the acquired certs.
cert_directory_prefix="/etc/letsencrypt/live/${server_name}"
if [ "$1" == "tls" ]; then
    cat <<EOF

ssl_certificate      ${cert_directory_prefix}/fullchain.pem;
ssl_certificate_key  ${cert_directory_prefix}/privkey.pem;
include              /etc/nginx/inc.d/ssl.conf;
include              /etc/nginx/inc.d/security_headers.conf;

server {
    listen       [::]:443 ssl default_server;
    listen       443 ssl default_server;
    return       444;
}

server {
    listen       [::]:443 http2 ssl;
    listen       443 http2 ssl;
    server_name  ${server_name};
    return       301 \$scheme://www.\$host\$request_uri;
}

server {
    listen       [::]:443 http2 ssl;
    listen       443 http2 ssl;
    server_name  www.${server_name} localhost 127.0.0.1;
    charset      utf-8;

    gzip             on;
    gzip_types       text/plain text/xml text/css application/javascript;
    gzip_min_length  1024;

    location / {
        uwsgi_pass web:8000;
        include /etc/nginx/uwsgi_params;
    }

    location /static {
        root /var/www/apparatus;

        location /static/CACHE {
            expires max;
            gzip_vary on;
            add_header Cache-Control "public, immutable";
            include    /etc/nginx/inc.d/security_headers.conf;
        }
    }

    location /media {
        root /var/www/apparatus;
    }

    location = /robots.txt {
        return 404;
    }

    location = /favicon.ico {
        return 404;
    }
}
EOF
fi
