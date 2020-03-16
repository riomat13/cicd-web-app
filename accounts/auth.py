#!/usr/bin/env python3
"""Handle authentication by token

Reference:
    https://medium.com/@yerkebulan199/django-rest-framework-drf-token-authentication-with-expires-in-a05c1d2b7e05
"""

from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


def expires_in(token):
    elapsed = timezone.now() - token.created
    return timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - elapsed


def token_expire_handler(token):
    is_expired = expires_in(token) < timedelta(seconds=0)

    if is_expired:
        token.delete()
        token = None
    return is_expired, token


class ExpiringTokenAuthentication(TokenAuthentication):
    def authentication_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User is not active')

        is_expired, token = token_expire_handler(token)

        if is_expired:
            raise AuthenticationFailed('Token is expired')

        return (token.user, token)
