#!/usr/bin/env python3

from django.urls import path

from .api import views as api_views


urlpatterns = [
    path('', api_views.ContentAPIView.as_view(), name='blog_list'),
    path('create/', api_views.ContentCreateAPIView.as_view(), name='blog_creation'),
]
