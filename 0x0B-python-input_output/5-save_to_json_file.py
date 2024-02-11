#!/usr/bin/python3
"""
saving in json rep
"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """
    saving in json rep
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
