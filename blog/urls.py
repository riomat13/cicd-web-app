#!/usr/bin/env python3

from django.urls import path

from .api import views as api_views


urlpatterns = [
    path('all',
         api_views.ContentAPIView.as_view(),
         name='blog_list'),
    path('all/headlines',
         api_views.ContentHeadlineAPIView.as_view(),
         name='blog_headlines'),
    path('item/<slug:slug>',
         api_views.ContentAPIView.as_view(),
         name='blog_item'),
    path('item/id/<str:uuid>',
         api_views.ContentAPIView.as_view(),
         name='blog_item_id'),
    path('create/',
         api_views.ContentCreateAPIView.as_view(),
         name='blog_creation'),
]
