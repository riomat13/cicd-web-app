#!/usr/bin/env python3

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import User
from .serializers import UserSerializer


class UserAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = ''

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        # check if user is superuser when requested user data
        # and request sender do not match
        if request.user.username != username \
                and not request.user.is_superuser:
            return Response({
                'detail': 'Prohibited to extract other user information'
            }, HTTP_401_UNAUTHORIZED)

        # return error if invalid request is received
        if username is None:
            return Response({
                'detail': 'Bad request'
            }, HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response({
                'detail': 'Target user does not exist'
            }, HTTP_400_BAD_REQUEST)

        return Response({
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email
        }, HTTP_200_OK)


class UserEditAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = ''

    def put(self, request, *args, **kwargs):
        data = request.data

        try:
            user = User.objects.get(username=request.user.username)
        except ObjectDoesNotExist:
            return Response({
                'detail': 'invalid request'
            }, HTTP_400_BAD_REQUEST)

        email = data.get('email')
        firstname = data.get('firstname')
        lastname = data.get('lastname')

        if email is not None:
            user.email = email
        if firstname is not None:
            user.first_name = firstname
        if lastname is not None:
            user.last_name = lastname

        try:
            user.save()
        except Exception as e:
            return Response({
                'detail': str(e)
            }, HTTP_400_BAD_REQUEST)

        return Response({
            'detail': 'successfully edited'
        }, HTTP_200_OK)
