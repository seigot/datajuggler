# -*- coding: utf-8 -*-

from datajuggler.serializer.abstract import AbstractSerializer

from urllib.parse import urlencode
from urllib.parse import parse_qs

import re


class QueryStringSerializer(AbstractSerializer):
    """
    This class describes a query-string serializer.
    """

    def __init__(self):
        super().__init__()

    def decode(self, s, **kwargs):
        flat = kwargs.pop("flat", True)
        qs_re = r"(?:([\w\-\%\+\.\|]+\=[\w\-\%\+\.\|]*)+(?:[\&]{1})?)+"
        qs_pattern = re.compile(qs_re)
        if qs_pattern.match(s):
            data = parse_qs(s)
            if flat:
                data = {key: value[0] for key, value in data.items()}
            return data
        raise ValueError(f"Invalid query string: {s}")

    def encode(self, d, **kwargs):
        data = urlencode(d, **kwargs)
        return data
