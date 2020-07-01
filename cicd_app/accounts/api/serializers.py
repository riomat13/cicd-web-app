#!/usr/bin/env python3

from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
