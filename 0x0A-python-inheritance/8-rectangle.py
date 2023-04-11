#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""This module has a class that inherits from another class.
The instantiation width width and height.
"""


class Rectangle(BaseGeometry):
    """Class Rectangle.
    It inherits from BaseGeometry, instantiation with
    width and height.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
