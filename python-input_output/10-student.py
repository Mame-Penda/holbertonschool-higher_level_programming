#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new_student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
            """Get a dictionary representation of the student."""
            if attrs is None:
                 return {key: self.__dict__[key] for key in sorted(self.__dict__)}
            new_dict = {}
            for key in sorted(attrs):
                if key in self.__dict__:
                  new_dict[key] = self.__dict__[key]
            return new_dict
