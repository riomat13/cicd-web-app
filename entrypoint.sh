#!/bin/sh

DB_ENGINE_NAME=$(echo ${DB_ENGINE} | awk -F'.' '{print $4}')

# wait for database being ready
if [ "$DB_ENGINE_NAME" = "postgresql" ]; then
  echo "Starting database..."

  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done

  echo "Database is up"
fi

# parse env file
if [ -f ".env.prod" ]; then
  while IFS= read -r line; do
    export $line
  done < .env.prod

  unset DB_HOST
  unset DB_ENGINE
fi

# initial setup
manage.py collectstatic --noinput
manage.py migrate --noinput
manage.py createsuperuser --noinput

# setup for logging
if [ ! -d "/app/logs" ]; then
  mkdir -p /app/logs
fi

touch /app/logs/gunicorn.log
touch /app/logs/gunicorn-access.log

tail -n 0 -f /app/logs/gunicorn.log &
tail -n 0 -f /app/logs/gunicorn-access.log &

exec "$@"
