#!/usr/bin/env python3

import os.path

from django.db import transaction
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import parsers
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from ..models import Content
from .serializers import BlogContentSerializer
from .parsers import ImageJsonMultiPartParser


class ContentAPIView(APIView):
    queryset = Content.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BlogContentSerializer
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.order_by('updated_at')

        data = []
        for query in queryset:
            data.append({
                'title': query.title,
                'slug': query.slug,
                'headline': query.headline,
                'body': query.body,
                'image': {
                    'path': os.path.join('./', settings.MEDIA_URL, query.image.name)
                },
                'created_at': query.created_at,
                'updated_at': query.updated_at

            })
        return Response(data, HTTP_200_OK)


class ContentCreateAPIView(APIView):
    permission_classes = (IsAdminUser,)
    parser_classes = (ImageJsonMultiPartParser, parsers.JSONParser)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        body = request.data.get('body')
        headline = request.data.get('headline')
        image = request.data.get('media')

        if image is None:
            return Response({
                'detail': 'no valid image is provided'
            }, HTTP_400_BAD_REQUEST)

        sid = transaction.savepoint()

        try:
            content = Content(title=title,
                              headline=headline,
                              body=body,
                              image=image)
            content.save()
        except Exception as e:
            transaction.savepoint_rollback(sid)
            return Response({
                'detail': 'failed content creation',
                'error': str(e)
            }, HTTP_400_BAD_REQUEST)

        return Response({
            'content': content.slug,
            'image': os.path.basename(image.name)
        }, HTTP_200_OK)
