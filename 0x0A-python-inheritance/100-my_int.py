#!/usr/bin/python3
"""This module inverts == and != operations.
The module has the Myint class.
"""


class MyInt(int):
    """Class MyInt.
    It inherits from int and :
    replaces == for !=  and replaces != for ==
    """

    def __ne__(*args):
        return True

    def __eq__(*args):
        return False
