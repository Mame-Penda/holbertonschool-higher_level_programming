#!/usr/bin/python3
""" Module for the BaseGeometry class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle which inherite a BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a rectangle height and width."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
