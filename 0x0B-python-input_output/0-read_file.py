#!/usr/bin/python3
"""
This module has one function read_file.
"""


def read_file(filename=""):
    """Function read_file.
    Reads a text file(UTF8) and prints in stdout.
    Args:
        filename: path to the file to be read.
    Returns:
        no return
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end='')

