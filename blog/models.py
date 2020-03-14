#!/usr/bin/env python3

import uuid

from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    content = models.TextField()
