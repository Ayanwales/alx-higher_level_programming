#!/usr/bin/python3
"""This module has a function wich creates new attributes.
"""


def add_attribute(self, name, new_attribute):
    """function add_attribute.
    It add a new attribute to an object.
    Args:
        name (str): new attribute
        new_attribute: value of new attribute
        self: object name
    Returns:
        not return
    """
    try:
        self.name = new_attribute
    except:
        raise TypeError("can't add new attribute")
