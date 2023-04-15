#!/usr/bin/python3
"""This module  has a Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle.
    the class defines the private instance attributes:
    __width, __height, __x, __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__
        init method to create each instance
        """
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if (type(x) != int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if (type(y) != int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    def area(self):
        """
        method to calculate the are of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        method to display # signs
        """
        s = "\n" * self.__y
        a = self.__width * "#" + "\n"
        b = " " * self.__x
        print(s + self.__height * (b + a), end="")

    def __str__(self):
        """
        method __str__ to format the print output
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        method to update an instance attributes
        """
        my_attris = ["id", "width", "height", "x", "y"]
        if args is not None and args != ():
            for i in range(len(my_attris)):
                if i < len(args):
                    setattr(self, my_attris[i], args[i])
        elif kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        method to convert return instance attributes in
        dictionary format
        """
        my_copy = {}
        for k, v in self.__dict__.items():
            my_copy[k] = v
        for key, value in my_copy.items():
            tem_atr = key.split("__")
            if len(tem_atr) > 1:
                clean_atr = tem_atr[1]
                my_copy[clean_atr] = value
                del my_copy[key]
        return my_copy

    @property
    def width(self):
        """
        return the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        update the given attribute""
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        update the height attribute
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        return the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        update the x attribute
        """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        return the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        update the y attribute
        """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
