# -*- coding: utf-8 -*-

import pytest

from datajuggler import Keypath
from datajuggler.dicthelper import d_search

data =  {
        "a": "January",
        "b": "january!",
        "c": {
            "d": True,
            "e": " january february ",
            "f": {
                "g": ['January', 'February', 'March', 'April' ],
                "january": 12345,
                "February": True,
            },
        },
        "x": "Peter Piper picked a peck of pickled peppers.",
        "y": { "x": { "y": 5, "z": 6, }, },
        "January February": "march",
    }

class TestClass:

    def test_search_case01(self):
        expect = {}
        result = d_search(data, "jarnuary", search_for="value")
        assert result == expect

    def test_search_case02(self):
        expect = {Keypath('a'): 'January',
                  Keypath('b'): 'january!',
                  Keypath('c.f.g[0]'): 'January'}
        result = d_search(data, "january",
                          search_for="value", ignore_case=True)
        assert result == expect

    def test_search_case03(self):
        expect = {}
        result = d_search(data, "january",
                          search_for="value", exact=True)
        assert result == expect

    def test_search_case04(self):
        expect = {Keypath("a"): 'January',
                  Keypath("b"): 'january!',
                  Keypath("c.f.g[0]"): 'January' }
        result = d_search(data, "january",
                          search_for="value", ignore_case=True)
        assert result == expect

    def test_search_case05(self):
        data =  {
            "a": "January",
            "b": "january!",
            "c": {
                "d": True,
                "e": " january february ",
                "f": {
                    "g": {1: 'January', 2: 'February' },
                    "january": 12345,
                    "February": True,
                },
            },
            "x": "Peter Piper picked a peck of pickled peppers.",
            "y": { "x": { "y": 5, "z": 6, }, },
            "January February": "march",
        }
        expect = {'a': 'January',
                  'b': 'january!',
                  'c.f.g[1]': 'January'}

        result = d_search(data, "january",
                         search_for="value",
                         ignore_case=True,
                         use_keypath=False)
        assert result == expect

