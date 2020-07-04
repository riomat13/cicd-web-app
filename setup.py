#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='cicd_app',
    version='0.0.1.dev0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    scripts=['scripts/manage.py'],
)
