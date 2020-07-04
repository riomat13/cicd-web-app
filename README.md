# CI/CD practice web application

This is a web application to practice CI/CD process with web application developed with `Django (==3.0.x)` and `Vue.js`.

## Execution
Deploy with `docker-compose`. `Postgresql` is used for database.
```
# Run docker container
# (Total image size is 320+MB including application, nginx, postgresql)
docker-compose up -d --build

# to check database
$ docker-compose db exec -U {username} -d {db_name} -W

# display db list
db_name=# \l

# choose db
db_name=# \c <db_name>

# Shut down and clean up containers
docker-compose down -v
```