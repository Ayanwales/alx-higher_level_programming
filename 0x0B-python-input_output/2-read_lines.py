#!/usr/bin/python3
"""
This module has one function read_lines.
"""


def read_lines(filename="", nb_lines=0):
    """Function read_lines.
    Reads and prints n lines in a text file(UTF8).
    Args:
        filename: path to the file to be read.
        nb_lines: number of lines to print and read
    Returns:
        No return
    """
    with open(filename, encoding="utf-8") as my_file:
        if (nb_lines <= 0):
            print(my_file.read(), end='')
        else:
            for i in range(nb_lines):
                if my_file is not "":
                    print(my_file.readline(), end='')
