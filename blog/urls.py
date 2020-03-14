#!/usr/bin/env python3

from django.urls import path, re_path

from . import views
from .api import views as api_views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api_views.ContentCreateAPIView.as_view(), name='blog_creation'),
    path('api/<str:uuid>/',
         api_views.ContentRetrieveUpdateDestroyAPIView.as_view(),
         name='blog_edit'),
    re_path(r'^(?:.*)/?$', views.index),
]
