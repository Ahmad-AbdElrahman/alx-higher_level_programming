#!/usr/bin/python3
"""
returns True if the object is an instance
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
