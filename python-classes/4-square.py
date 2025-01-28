#!/usr/bin/python3
""" This module creates a Square Class """


class Square:
    """
    Square class with size validation
    Area method to calculate the area of the square
    Property size to retrieve the size of the square
    Property position to retrieve the position of the square
    Size setter to set the size of the square
    Property position setter to set the position of the square
    Print method to print the square
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
