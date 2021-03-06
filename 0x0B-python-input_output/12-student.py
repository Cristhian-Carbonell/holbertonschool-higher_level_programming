#!/usr/bin/python3
"""
class Student that defines a student by: (based on 11-student.py)
"""


class Student:
    """
    Public instance attributes:
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self.attrs = attrs
        if type(attrs) is not list:
            return(self.__dict__)
        else:
            dicc = {}
            for index in attrs:
                if type(index) is str:
                    if index in self.__dict__.keys():
                        dicc[index] = self.__dict__.get(index)
            return(dicc)
