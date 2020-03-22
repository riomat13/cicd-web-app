#!/usr/bin/env python3

from django.test import TestCase

from accounts.models import User


class TestUserModel(TestCase):

    def test_superuser_creation(self):
        user = User.objects.create_superuser(
            username='superuser',
            password='test',
            email='test@example.com'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_user_creation(self):
        user = User.objects.create_user(
            username='user',
            password='test',
            email='test@example.com'
        )

        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
