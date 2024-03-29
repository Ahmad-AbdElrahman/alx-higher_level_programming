#!/usr/bin/python3
"""
Square Geometry calculation
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Geometry calculation
    """

    def __init__(self, size=0):
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
