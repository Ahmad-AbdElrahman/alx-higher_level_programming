#!/usr/bin/python3
"""
printing to stdout
"""


def read_file(filename=""):
    """
    printing to stdout
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
