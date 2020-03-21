#!/usr/bin/env python3

from rest_framework import serializers

from ..models import Content


class BlogContentSerializer(serializers.ModelSerializer):
    path = serializers.CharField(max_length=128)

    class Meta:
        model = Content
        fields = ['title', 'slug', 'uuid', 'headline', 'text', 'image', 'created_at', 'updated_at']
