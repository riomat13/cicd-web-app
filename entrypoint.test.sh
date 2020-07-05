#!/bin/sh

# parse env file
if [ -f ".env.prod" ]; then
  while IFS= read -r line; do
    export $line
  done < .env.test

  unset DB_HOST
  unset DB_ENGINE
fi

# initial setup
manage.py migrate --settings=cicd_app.settings.test --noinput

exec "$@"
