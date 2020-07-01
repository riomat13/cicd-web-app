# CI/CD practice web application

This is a web application to practice CI/CD process with web application developed with `Django` and `Vue.js`.


## Execution
- Local Execution
```
$ export HOME_DIR='/path/to/directory'

# run virtualenv

# for local development
$ ./run_test.sh

# or, run following 3 commands in different terminals
# run frontend app
$ cd $HOME_DIR/frontend
$ npm run serve

# run json-server for mock api
$ cd $HOME_DIR/frontend
$ npm run mock-server  # this requires json-server setup

$ cd $HOME_DIR
$ python3 manage.py runserver --settings=cicd_app.settings.local

# STATIC_URL is set to `/static/` so need to collect
$ manage.py collectstatic

# run with gunicorn
$ gunicorn cicd_app.wsgi:application --bind 0.0.0.0:8000
```

- Run on docker container
```
docker-compose up -d --build

# to check database
$ docker-compose db exec -U {username} -d {db_name} -W

# display db list
db_name=# \l

# choose db
db_name=# \c <db_name>
```