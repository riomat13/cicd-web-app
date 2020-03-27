#!/usr/bin/env python3

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .api.views import UserAPIView


urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('detail/<str:username>', UserAPIView.as_view(), name='user_profile')
]
