#!/bin/bash

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

    location / {
        uwsgi_pass apparatus;
        include /etc/nginx/uwsgi_params;
    }

    location /static {
        root /var/www/apparatus;
    }

    location /media {
        root /var/www/apparatus;
    }
}
EOF
fi
