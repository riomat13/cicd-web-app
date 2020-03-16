#!/usr/bin/env python3

from django.urls import re_path, include
from rest_framework.authtoken import views

from .api import views as api_views

urlpatterns = [
    re_path('^login/?$', api_views.login),
    re_path('^logout/?$', api_views.logout, name='logout')
]
