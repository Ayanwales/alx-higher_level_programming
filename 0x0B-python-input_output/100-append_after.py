#!/usr/bin/python3

"""
This module finds an string in a file an adds a line.
"""


def append_after(filename="", search_string="", new_string=""):
    """Function append_after.
    Adds an string after a given one is found
    Args:
        search_string(str): string to be searched in file.
        new_string: new string to add
    Returns:
        no return
    """
    with open(filename, mode="r+", encoding="utf-8") as my_file:
        my_line = my_file.readline()
        while my_line != "":
            if my_line.find(search_string) != -1:
                my_file.write(new_string)
            my_line = my_file.readline()
