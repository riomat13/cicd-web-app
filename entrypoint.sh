#!/bin/sh

cd /app/cicd_app
export DJANGO_SETTINGS_MODULE=settings.production

DB_ENGINE_NAME=$(echo ${DB_ENGINE} | awk -F'.' '{print $4}')

if [ "$DB_ENGINE_NAME" = "postgresql" ]; then
  echo "Starting database..."

  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done

  echo "Database is up"
fi

python manage.py migrate --no-input
python manage.py createsuperuser --noinput

if [ ! -d "/app/logs" ]; then
  mkdir logs
fi

touch /app/logs/gunicorn.log
touch /app/logs/gunicorn-access.log

tail -n 0 -f /app/logs/gunicorn.log &
tail -n 0 -f /app/logs/gunicorn-access.log &

exec "$@"
