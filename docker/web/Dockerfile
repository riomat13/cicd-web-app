##############################
#  Builder                   #
##############################
FROM python:3.8.3-alpine AS builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

RUN apk update \
    && apk add postgresql-dev \
        build-base \
        linux-headers \
        gcc \
        libffi-dev \
        python3-dev \
        musl-dev \
        libjpeg \
        jpeg-dev \
        zlib-dev \
    && pip install --upgrade pip \
    && pip install flake8

COPY . /app/
RUN flake8 --ignore=E501,F401,F403,F405 .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

ENV PYTHONPATH /app/cicd_app

##############################
#  Main                      #
##############################
FROM python:3.8.3-alpine

ENV APP_HOME /app

RUN mkdir -p $APP_HOME/static $APP_HOME/media/images
WORKDIR $APP_HOME

RUN addgroup -S app && adduser -S user -G app

RUN apk update \
    && apk add libpq libjpeg

COPY --from=builder /app/wheels /wheels

COPY . /app/
RUN pip install --no-cache /wheels/* \
    && pip install .

ENTRYPOINT ["./entrypoint.sh"]

RUN chown -R user:app $APP_HOME
USER user
