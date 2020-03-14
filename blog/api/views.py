#!/usr/bin/env python3

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated


from ..models import Content
from .serializers import ContentSerializer


class ContentCreateAPIView(ListCreateAPIView):
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ContentSerializer
    lookup_field = 'uuid'


class ContentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ContentSerializer
    lookup_field = 'uuid'
