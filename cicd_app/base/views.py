#!/usr/bin/env python3

from django.shortcuts import render


def index(request):  # pragma: no cover
    return render(request, 'index.html')
