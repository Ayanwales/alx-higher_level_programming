#!/usr/bin/python3

"""
This module transform object class into JSON format.
"""


def class_to_json(obj):
    """Function class_to_json.
    Returns the JSON representation of a class.
    Args:
        obj: object whose clase will be represented.
    Returns:
        JSON representation
    """
    return obj.__dict__
