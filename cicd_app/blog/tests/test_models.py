#!/usr/bin/env python3

import io
from unittest.mock import patch

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from blog.models import Content


class TestContent(TestCase):

    TITLE = 'test title'
    HEADLINE = 'test headline'
    BODY = 'This is test content'

    def create_content(self):
        # mocking empty image file
        img_file = io.BytesIO()
        img_file.name = 'test.png'
        img_file.seek(0)

        f = SimpleUploadedFile(img_file.name, img_file.read())

        before = Content.objects.count()
        content = Content.objects.create(
            title=self.TITLE,
            headline=self.HEADLINE,
            body=self.BODY,
            image=f
        )

        self.assertEqual(Content.objects.count(), before + 1)
        return content.id

    def test_blog_content_creation(self):
        id = self.create_content()

        content = Content.objects.get(id=id)

        # all data image file name must starts with 'image/blog/'
        self.assertTrue(content.image.name.startswith('images/blog/'))

    def test_blog_content_update(self):
        new_title = 'new title'
        id = self.create_content()

        content = Content.objects.get(id=id)
        updated = content.updated_at
        content.title = new_title

        content.save()

        self.assertGreater(content.updated_at, updated)

        content = Content.objects.get(id=id)
        self.assertEqual(content.title, new_title)

    @patch('blog.models.os.remove')
    def test_blog_content_deletion(self, remove):
        id = self.create_content()

        content = Content.objects.get(id=id)
        path = content.image.path

        content.delete()

        # must be removed both content and image data
        with self.assertRaises(ObjectDoesNotExist):
            Content.objects.get(id=id)

        # correspond image file is also removed
        remove.assert_called_once_with(path)

    def test_blog_content_extraction(self):
        pass
