#!/usr/bin/python3
"""
adding new attributes to objects
"""


def add_attribute(obj, attrname, attrvalue):
    """
    adding new attributes to objects
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attrname, attrvalue)
    else:
        raise TypeError("can't add new attribute")
