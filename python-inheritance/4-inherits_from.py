#!/usr/bin/python3
"""Defines a class_checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
    obj (any): The object to check.
    a_class (type): The class to compare.
    Returns:
    if obj is an instance or inherited instance of a_class _ True.
    Otherwise _ False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
