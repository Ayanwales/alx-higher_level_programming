#!/usr/bin/python3
""" My class Student
"""


class Student:
    """ My class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dic = {}
        if attrs is None:
            return self.__dict__
        copy_dic = self.__dict__
        for k, v in copy_dic.items():
            if k in attrs:
                my_dic[k] = v
        return my_dic

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
