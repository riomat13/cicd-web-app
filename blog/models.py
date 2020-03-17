#!/usr/bin/env python3

import uuid

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Content(models.Model):
    title = models.CharField(max_length=128, blank=False)
    slug = models.SlugField(unique=True)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    headline = models.CharField(max_length=256, blank=True)
    img = models.CharField(max_length=128, blank=True)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(editable=False, null=True)
    updated_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        now = timezone.now()
        if not self.id:
            self.created_at = now
        self.updated_at = now
        return super(Content, self).save(*args, **kwargs)
