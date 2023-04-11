#!/usr/bin/python3
"""This module determines if a object is and instance
of a given class that inherited from a spacified class.
The module has the function inherits_from.
"""


def inherits_from(obj, a_class):
    """function inherits_from.
    It returns True or False pending if the given object
    is an instance of a class that inherits from given class.
    Args:
        obj: object to be evaluated
        a_class: class to be evaluated
    Returns:
        True or False
    """
    if (isinstance(obj, a_class) is True and type(obj) != a_class):
        return (True)
    else:
        return (False)
