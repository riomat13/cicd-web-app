#!/usr/bin/env python3

import io

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from blog.models import Content


#class ContentModelTest(TestCase):
#
#    def setUp(self):
#        # mocking empty image file
#        img_file = io.BytesIO()
#        img_file.name = 'test.png'
#        img_file.seek(0)
#
#        BlogImage.objects.create(
#            data=SimpleUploadedFile(
#                name=img_file.name,
#                content=img_file.read(),
#                content_type='image/jpeg'
#            )
#        )
#
#    def test_content_item_creation(self):
#        try:
#            with transaction.atomic():
#                Content.objects.create(
#                    headline='test headline1',
#                    body='this is test1.'
#                )
#        except IntegrityError:
#            # must not be save due to lacking title
#            pass
#
#        try:
#            with transaction.atomic():
#                Content.objects.create(
#                    title='test1',
#                    headline='test headline1',
#                    body='this is test1.'
#                )
#        except IntegrityError:
#            # must not be save due to lacking image
#            pass
#
#        img = BlogImage.objects.first()
#
#        # should be success
#        with transaction.atomic():
#            Content.objects.create(
#                title='test1',
#                headline='test headline1',
#                body='This is test1.',
#                image_id=img.id,
#            )
#
#        self.assertEqual(Content.objects.count(), 1)
#
#        content = Content.objects.first()
#
#        # slug and uuid must be given after creation
#        self.assertTrue(content.slug)
#        self.assertTrue(content.uuid)
