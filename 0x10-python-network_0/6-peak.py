#!/usr/bin/python3
"""Determine one peak in agiven array"""


def find_peak(list_of_integers):
    """returns one peak in a given array"""
    if len(list_of_integers) != 0 and list_of_integers is not None:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
