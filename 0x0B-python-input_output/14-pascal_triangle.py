#!/usr/bin/python3

"""
This module transform return pascal triangle.
"""


def pascal_triangle(n):
    """Function pascal_triangle.
    Returns returns a list of list with integers that
    represent the pascal triangle.
    Args:
        n (int): size of the triangle.
    Returns:
        list of list
    """
    my_row1 = []
    my_matrix = []
    my_row = [1]
    my_matrix.append(my_row)
    if n <= 0:
        return my_row1
    if n >= 2:
        my_row = [1, 1]
        my_matrix.append(my_row)
        for i in range(3, n + 1):
            my_row1.append(1)
            for j in range(len(my_row) - 1):
                my_row1.append(my_row[j] + my_row[j + 1])
            my_row1.append(1)
            my_matrix.append(my_row1)
            my_row = my_row1
            my_row1 = []
    return my_matrix
