#!/usr/bin/python3
import json

"""
This module has one function to_json_string.
"""


def to_json_string(my_obj):
    """Function to_json_string.
    Returns the JSON representation of a object(string).
    Args:
        my_obj: object to be represented.
    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
