#!/bin/bash

apparatus_media_dir=/var/www/apparatus/media
if [ ! -d $apparatus_media_dir ]; then
    mkdir -p $apparatus_media_dir
    chown uwsgi:uwsgi $apparatus_media_dir
fi

python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py compress
exec uwsgi --uid uwsgi --socket :8000 --protocol uwsgi --module apparatus.wsgi
