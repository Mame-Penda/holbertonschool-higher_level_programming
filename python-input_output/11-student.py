#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
        first_name (str): The first name of student.
        last_name (str): last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.

            Args:
            attrs (list, optional): The attributes to represent.

            Returns:
            dict: dictionaire that contains all informations.
            """
        if attrs is None:
            return {
                    self.first_name: "first_name",
                    self.last_name: "last_name",
                    self.age: "age"
                }
        else:
            result = {}
        for attr in attrs:
         if hasattr(self, attr):
            result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """Replace all attributes of the student.

                        Args:
                        json (dict): The key/value pairs to replace attibutes.
                        """
        for key, value in json.items():
         if hasattr(self, key):
            setattr(self, key, value)
