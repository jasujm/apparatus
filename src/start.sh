#!/bin/bash

# Wait for mysql before attempting to migrate and un the app
waittime=1
until nc -z -w30 mysql 3306; do
    echo 'Waiting for mysql...'
    sleep $waittime;
    waittime=$((waittime*2))
    waittime=$((waittime<32 ? waittime : 32))
done

apparatus_media_dir=/var/www/apparatus/media
if [ ! -d $apparatus_media_dir ]; then
    mkdir -p $apparatus_media_dir
    chown uwsgi:uwsgi $apparatus_media_dir
fi

python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py compress
exec uwsgi --uid uwsgi --socket :8000 --protocol uwsgi --module apparatus.wsgi
