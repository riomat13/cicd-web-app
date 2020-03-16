#!/usr/bin/env python3

from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

from ..auth import expires_in, token_expire_handler
from ..models import User
from .serializers import UserSerializer, UserLogInSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    login_serializer = UserLogInSerializer(data=request.data)

    if not login_serializer.is_valid():
        return Response(login_serializer.errors, status=HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=login_serializer.data['username'],
        password=login_serializer.data['password']
    )
    if not user:
        return Response(
            {'detail': 'Invalid credential or active account'},
            status=HTTP_404_NOT_FOUND
        )

    token, _ = Token.objects.get_or_create(user=user)

    is_expired, token = token_expire_handler(token)

    if is_expired:
        # recreate token if expired
        token = Token.objects.create(user=user)
    else:
        # if not expired, extend time of token alive
        token.created = timezone.now()

    user_selialized = UserSerializer(user)

    return Response({
        'user': user_selialized.data,
        'expires_in': expires_in(token),
        'token': token.key
    }, status=HTTP_200_OK)


@api_view(['DELETE'])
def logout(request):
    try:
        user = User.objects.get(username=request.data.get('username'))
    except User.DoesNotExist:
        return Response(
            {'detail': 'Invalid credentials or active account'},
            status=HTTP_404_NOT_FOUND
        )

    token = Token.objects.get(user=user)
    if token is not None:
        token.delete()

    return Response({
        'detail': 'removed login status'
    }, status=HTTP_200_OK)
