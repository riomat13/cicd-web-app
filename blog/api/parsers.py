#!/usr/bin/env python3

import json

from django.http import QueryDict
from rest_framework import parsers


class ImageJsonMultiPartParser(parsers.MultiPartParser):
    """Parse image and json content simultaneously.

    Reference:
        https://stackoverflow.com/questions/30176570/using-django-rest-framework-how-can-i-upload-a-file-and-send-a-json-payload
    """

    def parse(self, stream, media_type=None, parser_context=None):
        parsed = super(ImageJsonMultiPartParser, self) \
            .parse(stream, media_type=media_type, parser_context=parser_context)

        data = {}
        if parsed.data.get('data'):
            data = json.loads(parsed.data.get('data'))

        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)

        # replace data in DataAndFile object to new dataset
        parsed.data = query_dict

        return parsed
