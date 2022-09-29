#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
    """Initialize a new Student.
    Args:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
        attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):
            new = dict()
            for x in attrs:
                if x in self.__dict__:
                    new.update({x: self.__dict__[x]})
                    return new
                return self.__dict__

     def reload_from_json(self, json):
     """reload json
     replaces all attributes of the student instance.
     """
     for x in json:
         self.__dict__[x] = json[x]
