#!/usr/bin/python3
import json

"""
This module has one function from_json_string(my_str).
"""


def from_json_string(my_str):
    """Function from_json_string.
    Returns an object(Python data struct) represented by a JSON string.
    Args:
        my_str: object to be represented.
    Returns:
        Python object representation
    """
    return json.loads(my_str)
