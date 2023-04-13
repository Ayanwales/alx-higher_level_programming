#!/usr/bin/python3
"""
This module has one function number_of_lines.
"""


def number_of_lines(filename=""):
    """Function number_of_lines.
    Returns the number of lines in a text file(UTF8).
    Args:
        filename: path to the file to be read.
    Returns:
        Number of lines in fila
    """
    count = 0
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            count += 1
        return count
