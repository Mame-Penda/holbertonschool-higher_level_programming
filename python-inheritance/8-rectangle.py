#!/usr/bin/python3
"""Defines a class_checking function."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle which inherite a BaseGeometry.
    """
    def __init__(self, width, height):
     """Initialize a rectangle height and width.
    """
     self.integer_validator("width", width)
     self.integer_validator("height", height)
     self.__width = width
     self.__height = height
