#!/bin/bash

# Monkey patching migrations that have too long keys
sed -i s/767/752/g /usr/local/lib/python3.8/site-packages/djangocms_blog/migrations/0036_auto_20180913_1809.py
sed -i s/767/752/g /usr/local/lib/python3.8/site-packages/djangocms_blog/migrations/0032_auto_20180109_0023.py

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
exec uwsgi --uid uwsgi --socket :8000 --protocol uwsgi --module apparatus.wsgi
