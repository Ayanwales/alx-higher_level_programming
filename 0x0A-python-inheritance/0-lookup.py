#!/usr/bin/python3
"""This module has returns the attributes and methods of object.
The module has the function lookup.
"""


def lookup(obj):
    """Function lookup().
    The lookup function retorn the attributes
    and methos of a given object.
    Args:
        obj (obj): to be evaluated
    Returns:
        list of attributes and methods of object
    """
    return (dir(obj))
