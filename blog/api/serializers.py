#!/usr/bin/env python3

from rest_framework import serializers

from ..models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'slug', 'uuid', 'headline', 'text', 'img', 'created_at', 'updated_at']
