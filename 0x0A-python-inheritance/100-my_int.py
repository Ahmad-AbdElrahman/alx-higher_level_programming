#!/usr/bin/python3
"""
My int rebel class
"""


class MyInt(int):
    """
    My int rebel class
    """
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other_int):
        if self.__value == other_int:
            return False

    def __ne__(self, other_int):
        if self.__value == other_int:
            return True
