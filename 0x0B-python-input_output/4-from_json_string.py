#!/usr/bin/python3
"""
from json to python
"""


from json import loads


def from_json_string(my_str):
    """
    representation in json
    """

    return loads(my_str)
