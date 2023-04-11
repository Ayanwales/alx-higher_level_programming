#!/usr/bin/python3
"""This module has a class that inherits from list.
The module has the Mylist class.
"""


class MyList(list):
    """Class Mylist.
    It inherits from list and has the:
    print_sorted method that prints a list bur sorted
    ascending.
    Args:
        obj: it evaluates an object
    Returns:
        no returns
    """
    def print_sorted(self):
        my_copy = self[:]
        my_copy.sort()
        print(my_copy)
