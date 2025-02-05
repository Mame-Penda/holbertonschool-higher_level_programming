#!/usr/bin/python3
"""Module for the BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Method that initialize the rectangle.

        Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def area(self):
            """Method that returns the area of rectangle."""
            return self.__width * self.__height

        def __str__(self):
            """Method that returns the rectangle description."""
            string = "[" + str(self.__class__.__name) + "]"
            string += str(self.__width) + "/" + str(self.__height)
            return string
