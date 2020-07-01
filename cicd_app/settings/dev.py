#!/usr/bin/env python3

from .base import *


DEBUG = True

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': 'devuser',
    }
}
