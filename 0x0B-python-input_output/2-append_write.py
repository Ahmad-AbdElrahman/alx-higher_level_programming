#!/usr/bin/python3
"""
appending to file
"""


def append_write(filename="", text=""):
    """
    appending to file
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
