#!/usr/bin/env python3

import io

from django.db import transaction
from django.test import TestCase

from rest_framework.test import APIClient

from ..models import BlogImage, Content
from accounts.models import User


ADMIN_NAME = 'test'
ADMIN_EMAIL = 'test@example.com'
ADMIN_PASSWORD = 'test'

USERNAME = 'user'
USER_EMAIL = 'testuser@example.com'
USER_PASSWORD = 'user'

admin = None
user = None


def setUpModule():
    global admin
    global user

    admin = User.objects.create_superuser(
        username=ADMIN_NAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD,
        is_superuser=True,
        is_staff=True
    )

    user = User.objects.create_user(
        username=USERNAME,
        email=USER_EMAIL,
        password=USER_PASSWORD,
        is_superuser=False,
        is_staff=True
    )


class BlogApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        admin.is_active = False
        admin.save()
        user.is_active = False
        user.save()

    def get_login_token(self):
        admin.is_active = True
        admin.save()

        response = self.client.post(
            '/api/account/login/token/',
            {'username': ADMIN_NAME, 'password': ADMIN_PASSWORD},
            format='json'
        )
        return response.data.get('access')

    def create_image(self):
        # setup mock image
        img_file = io.BytesIO()
        img_file.name = 'test.png'
        img_file.seek(0)
        return img_file

    def test_blog_item_creation(self):
        # test without authentication
        response = self.client.post(
            '/api/blog/create/',
            {
                'title': 'Test Title',
                'headline': 'Lorem',
                'text': 'Lorem ipsum dolor sit amet'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, 401)

        token = self.get_login_token()

        response = self.client.post(
            '/api/blog/create/',
            data={
                'title': 'Test Title',
                'headline': 'Lorem',
                'text': 'Lorem ipsum dolor sit amet'
            },
            media='',
            HTTP_AUTHORIZATION=f'Bearer {token}',
            format='multipart'
        )

        # no image is provided
        self.assertEqual(response.status_code, 400)

        # setup mock image file to upload
        img_data = self.create_image()

        # test for working api (send and data creation)
        # this cannot test nested data
        # so test with postman as funcitonal test instead
        with transaction.atomic():
            response = self.client.post(
                '/api/blog/create/',
                {
                    'title': 'Test Title',
                    'headline': 'Lorem',
                    'text': 'Lorem ipsum dolor sit amet',
                    'media': img_data,
                },
                HTTP_AUTHORIZATION=f'Bearer {token}',
                format='multipart'
            )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Content.objects.count(), 1)
