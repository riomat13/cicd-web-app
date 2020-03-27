#!/usr/bin/env python3

from django.test import TestCase

from rest_framework.test import APIClient

from accounts.models import User


ADMIN_NAME = 'test-account'
ADMIN_EMAIL = 'test-account@example.com'
ADMIN_PASSWORD = 'test'

USERNAME = 'user-account'
USER_EMAIL = 'testuser-account@example.com'
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


class UserAPIViewTest(TestCase):

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

    def get_user_login_token(self):
        user.is_active = True
        user.save()

        response = self.client.post(
            '/api/account/login/token/',
            {'username': USERNAME, 'password': USER_PASSWORD},
            format='json'
        )
        return response.data.get('access')

    def check_valid_user_data(self, response, user):
        data = response.data
        if data is None:
            self.fail('No data received')

        self.assertEqual(data.get('username'), user.username)
        self.assertEqual(data.get('firstname'), user.first_name)
        self.assertEqual(data.get('lastname'), user.last_name)
        self.assertEqual(data.get('email'), user.email)

    def test_user_profile_extraction_by_user(self):
        # test without authentication
        response = self.client.get(f'/api/account/detail/{user.username}')

        self.assertEqual(response.status_code, 401)

        token = self.get_user_login_token()

        response = self.client.get(
            f'/api/account/detail/{user.username}',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.assertEqual(response.status_code, 200)
        self.check_valid_user_data(response, user)

        # extract data of non-requester
        # this is prohibited unless superuser is requesting
        # and return 401(unauthorized)
        response = self.client.get(
            f'/api/account/detail/{admin.username}',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.assertEqual(response.status_code, 401)

    def test_user_profile_extraction_by_admin(self):
        # can extract any user information by superuser
        token = self.get_login_token()

        response = self.client.get(
            f'/api/account/detail/{admin.username}',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.assertEqual(response.status_code, 200)
        self.check_valid_user_data(response, admin)

        response = self.client.get(
            f'/api/account/detail/{user.username}',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.assertEqual(response.status_code, 200)
        self.check_valid_user_data(response, user)

        # test to extract non-exist user
        response = self.client.get(
            f'/api/account/detail/non-exist-user',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.assertEqual(response.status_code, 400)
