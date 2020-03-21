#!/usr/bin/env python3

from django.contrib import admin

from .models import BlogImage, Content


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass
