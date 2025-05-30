#!/usr/bin/python3
""" This module creates a Class Rectangle that defines a rectangle."""


class Rectangle:
    """
    class Rectangle that defines a rectangle.
    Properties: width and height.
    Area and Perimeter methods.
    Print, str, repr and del methods.
    Number of instances.
    Number of instances and Print symbol.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1
        self.__class__.print_symbol = self.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        str = ""
        for i in range(self.__height):
            str += "{}".format(self.print_symbol) * self.__width
            str += "\n" if i != self.__height - 1 else ""
        return str

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print('Bye rectangle...')
        self.__class__.number_of_instances -= 1
        return
