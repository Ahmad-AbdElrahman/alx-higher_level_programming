#!/usr/bin/python3
"""
writing to file
"""


def write_file(filename="", text=""):
    """
    writing to file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
