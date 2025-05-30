#!/usr/bin/python3
"""Defines a class_checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
    obj: The object to check.
    a_class: The class to match the type of obj to.

    Returns:
    bool: True if object is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
