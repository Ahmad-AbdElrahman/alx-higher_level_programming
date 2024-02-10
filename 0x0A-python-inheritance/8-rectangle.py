#!/usr/bin/python3
"""
Geometry calculation
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Checks a integer value

    Args:
        name (str): The name of the value.
        value (int): The value.

    Raises:
        TypeError: If `value` isn't a integer.
        ValueError: If `value` is less than or equal to zero.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
