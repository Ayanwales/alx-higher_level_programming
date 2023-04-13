#!/usr/bin/python3
"""
This module has one function writes_file.
"""


def write_file(filename="", text=""):
    """Function write_file.
    Writes an string into a text file(UTF8).
    Args:
        filename: path to the file to be read.
        text: text to be added to the file
    Returns:
        number of characteres written
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        nc = my_file.write(text)
        return nc
