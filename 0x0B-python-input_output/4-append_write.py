#!/usr/bin/python3
"""
This module has one function append_write.
"""


def append_write(filename="", text=""):
    """Function append_write.
    Append a string at the end of a text file(UTF8).
    If file does not exist, it should create it
    Args:
        filename: path to the file to be read.
        text: text to be added to the file
    Returns:
        number of characteres added
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        nc = my_file.write(text)
        return nc
