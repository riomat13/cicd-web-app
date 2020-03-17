#!/usr/bin/env python3

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .api import views as api_views


urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
