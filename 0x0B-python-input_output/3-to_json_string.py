#!/usr/bin/python3
"""
representation in json
"""


from json import dumps


def to_json_string(my_obj):
    """
    string to json representation
    """

    return dumps(my_obj)
