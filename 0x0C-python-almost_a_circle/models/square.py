#!/usr/bin/python3
"""This module  has a Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square.
    the class defines the private instance attributes:
    __width, __height, __x, __y, setter and getter for size
    to_dictionary, update public methods.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        module pass values to super class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        module gives format to the print func
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        this module update the attributes of
        an instance
        """
        my_attris = ["id", "size", "x", "y"]
        if args is not None and args != ():
            for i in range(len(my_attris)):
                if i < len(args):
                    setattr(self, my_attris[i], args[i])
        elif kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key in my_attris:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        this module returns a dictionaty with the
        attributes of an instance
        """
        new_dir = {}
        copy_dir = self.__dict__
        for k, v in self.__dict__.items():
            attr_sq = k.split("__")
            if len(attr_sq) > 1:
                if attr_sq[1] == "width" or attr_sq[1] == "height":
                    attr_sq[1] = "size"
                clear_attr = attr_sq[1]
            else:
                clear_attr = attr_sq[0]
            new_dir[clear_attr] = v
        return new_dir

    @property
    def size(self):
        """
        this module return the size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        this module updates the attributes os an instance
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
