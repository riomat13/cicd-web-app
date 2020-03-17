#!/usr/bin/env python3

from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from ..models import Content
from .serializers import ContentSerializer


class ContentAPIView(ListAPIView):
    queryset = Content.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ContentSerializer
    lookup_field = 'uuid'


class ContentCreateAPIView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ContentSerializer

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        text = request.data.get('text')
        headline = request.data.get('headline')
        img = request.data.get('img')

        try:
            content = Content(title=title, headline=headline, text=text, img=img)
            content.save()
        except Exception as e:
            return Response({
                'detail': 'failed content creation',
                'error': str(e)
            }, HTTP_400_BAD_REQUEST)

        serialized = ContentSerializer(content)

        return Response({
            'content': serialized.data
        }, HTTP_200_OK)
