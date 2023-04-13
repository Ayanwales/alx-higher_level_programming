#!/usr/bin/python3
import json

"""
This module has one function load_from_json_file.
"""


def load_from_json_file(filename):
    """Function load_from_json_file.
    creates and object from a JSON file.
    Args:
        filename: JSON file.
    Returns:
        the created object
    """
    with open(filename, encoding="utf-8") as my_file:
        _str = my_file.read()
        return json.loads(_str)
