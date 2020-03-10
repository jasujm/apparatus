#!/bin/bash

cat > /etc/nginx/conf.d/default.conf <<EOF
server {
    listen       [::]:80 default_server;
    listen       80 default_server;
    return       444;
}

server {
    listen       [::]:80;
    listen       80;
    server_name  .${SERVER_NAME} localhost 127.0.0.1;

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
cert_directory_prefix="/etc/letsencrypt/live/${SERVER_NAME}"
fullchain_file="${cert_directory_prefix}/fullchain.pem"
privkey_file="${cert_directory_prefix}/privkey.pem"
if [ -f "$fullchain_file" -a -f "${privkey_file}" ]; then
    cat > /etc/nginx/conf.d/apparatus.conf <<EOF
ssl_certificate      ${fullchain_file};
ssl_certificate_key  ${privkey_file};
include              /etc/nginx/conf.d/include/ssl.conf;

server {
    listen       [::]:443 ssl default_server;
    listen       443 ssl default_server;
    return       444;
}

server {
    listen       [::]:443 http2 ssl;
    listen       443 http2 ssl;
    server_name  ${SERVER_NAME};
    return       301 \$scheme://www.\$host\$request_uri;
}

server {
    listen       [::]:443 http2 ssl;
    listen       443 http2 ssl;
    server_name  www.${SERVER_NAME} localhost 127.0.0.1;
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
