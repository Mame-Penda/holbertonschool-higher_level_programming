#!/usr/bin/python3
"""
This module provides a function to add two numbers
after validating their types. It ensures inputs are integers
or floats before performing the addition.
"""


def add_integer(a, b=98):
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
