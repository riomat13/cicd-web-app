#!/usr/bin/env python3

from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test-db',
        'HOST': 'localhost'
    }
}
