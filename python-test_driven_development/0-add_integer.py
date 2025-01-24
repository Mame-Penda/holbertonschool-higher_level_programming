#!/usr/bin/python3
"""
This module provides a function to add two numbers
after validating their types. It ensures inputs are integers
or floats before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers as integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers rounded to the nearest integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Use round() to ensure proper rounding
    return int(round(a)) + int(round(b))
