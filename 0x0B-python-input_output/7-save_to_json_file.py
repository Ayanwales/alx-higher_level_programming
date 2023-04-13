#!/usr/bin/python3
import json

"""
This module has one function save_to_json_file.
"""


def save_to_json_file(my_obj, filename):
    """Function save_to_json_file.
    Writes an object to a texfile using JSON representation.
    Args:
        my_obj: object to be saved.
    Returns:
        Does not return
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
