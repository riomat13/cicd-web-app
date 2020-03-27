#!/usr/bin/env python3

import io

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from django.test import TestCase

from rest_framework.test import APIClient

from blog.models import Content
from accounts.models import User


ADMIN_NAME = 'test-blog'
ADMIN_EMAIL = 'test@-blogexample.com'
ADMIN_PASSWORD = 'test'

USERNAME = 'user-blog'
USER_EMAIL = 'testuser-blog@example.com'
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


def create_image():
    # setup mock image
    img_file = io.BytesIO()
    img_file.name = 'test.png'
    img_file.seek(0)
    return img_file


class BlogCreationAPITest(TestCase):

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

    def test_blog_item_creation(self):
        # test without authentication
        response = self.client.post(
            '/api/blog/create/',
            {
                'title': 'Test Title',
                'headline': 'Lorem',
                'body': 'Lorem ipsum dolor sit amet'
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
                'body': 'Lorem ipsum dolor sit amet'
            },
            media='',
            HTTP_AUTHORIZATION=f'Bearer {token}',
            format='multipart'
        )

        # no image is provided
        self.assertEqual(response.status_code, 400)

        # setup mock image file to upload
        img_data = create_image()

        # test for working api (send and data creation)
        # this cannot test nested data
        # so test with postman as funcitonal test instead
        with transaction.atomic():
            response = self.client.post(
                '/api/blog/create/',
                {
                    'title': 'Test Title',
                    'headline': 'Lorem',
                    'body': 'Lorem ipsum dolor sit amet',
                    'media': img_data,
                },
                HTTP_AUTHORIZATION=f'Bearer {token}',
                format='multipart'
            )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Content.objects.count(), 1)


class BlogExtractionAPITest(TestCase):

    def create_content(self, n=1):
        img_file = create_image()

        for i in range(n):
            f = SimpleUploadedFile(img_file.name, img_file.read())

            Content.objects.create(
                title=f'{i+1}-th title',
                headline=f'{i+1}-th test headline',
                body=f'{i+1}-th test content',
                image=f,
            )

    def test_item_list(self):
        target_count = 5
        self.create_content(target_count)

        # target attributes shoud be included in return items
        attrs = ['title', 'headline', 'body', 'image', 'created_at', 'updated_at']
        response = self.client.get('/api/blog/all')

        self.assertEqual(response.status_code, 200)

        data = response.data

        # check extracted data count is correct
        self.assertEqual(len(data), target_count)
        self.assertEqual(len(data), Content.objects.count())

        # check all extracted items have expected attributes
        for query in data:
            keys = set(query.keys())

            for attr in attrs:
                self.assertIn(attr, keys)

            self.assertIn('path', query.get('image'))

    def test_item_headline_list(self):
        target_count = 5
        self.create_content(target_count)

        # target attributes shoud be included in return items
        attrs = ['title', 'headline', 'image', 'created_at', 'updated_at']
        response = self.client.get('/api/blog/all/headlines')

        self.assertEqual(response.status_code, 200)

        data = response.data

        # check extracted data count is correct
        self.assertEqual(len(data), target_count)
        self.assertEqual(len(data), Content.objects.count())

        # check all extracted items have expected attributes
        for query in data:
            keys = set(query.keys())

            for attr in attrs:
                self.assertIn(attr, keys)

            self.assertNotIn('body', keys)

            self.assertIn('path', query.get('image'))

    def test_extract_item(self):
        self.create_content(1)

        content = Content.objects.first()

        # target attributes shoud be included in return items
        attrs = ['title', 'headline', 'body', 'image', 'created_at', 'updated_at']

        # extract item by slug
        response = self.client.get(f'/api/blog/item/{content.slug}')

        self.assertEqual(response.status_code, 200)

        data = response.data

        # check all extracted items have expected attributes
        keys = set(data.keys())

        for attr in attrs:
            self.assertIn(attr, keys)

        self.assertIn('path', data.get('image'))

        # content is sent after processed by paragraph
        body = content.body.split('\n')

        self.assertEqual(content.title, data.get('title'))
        self.assertEqual(content.headline, data.get('headline'))
        self.assertEqual(len(body), len(data.get('body')))
        self.assertEqual(body[0], data.get('body')[0])

        # extract item by uuid
        response = self.client.get(f'/api/blog/item/id/{content.uuid}')
        self.assertEqual(response.status_code, 200)

        data = response.data
        self.assertEqual(content.title, data.get('title'))
        self.assertEqual(content.headline, data.get('headline'))
        self.assertEqual(len(body), len(data.get('body')))
        self.assertEqual(body[0], data.get('body')[0])

        # handle non-exist api request
        response = self.client.get(f'/api/blog/item/not-exist-slug')
        self.assertEqual(response.status_code, 200)

        # return empty item
        self.assertFalse(response.data)
