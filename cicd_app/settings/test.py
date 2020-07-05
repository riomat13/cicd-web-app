#!/usr/bin/env python3

from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test.db',
        'HOST': 'localhost'
    }
}
