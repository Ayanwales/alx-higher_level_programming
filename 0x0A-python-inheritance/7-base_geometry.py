#!/usr/bin/python3
"""This module has a class and twa method.
The module has the BaseGeometry class, the
area method, and integer_validator method.
"""


class BaseGeometry():
    """Class BaseGeometry.
    It has a method area which is
    not implemented yet. It has the integer
    validator method.
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError("{0!s} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{0!s} must be greater than 0".format(name))
