#!/usr/bin/python3
"""
loads in json rep
"""


from json import loads


def load_from_json_file(filename):
    """
    loads in json rep
    """

    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
