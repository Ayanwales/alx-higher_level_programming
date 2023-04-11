#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""This module has a class that inherits from another class.
The instantiation size, it has the method area.
"""


class Square(Rectangle):
    """Class Square.
    It inherits from Rectangle, instantiation size,
    it has the method area.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
