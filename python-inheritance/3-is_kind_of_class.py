#!/usr/bin/python3
"""Defines a class_checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to.
    Returns:
    if obj is an instance or inherited instance of a_class _ True.
    Otherwise _ False.
    """
    if isinstance(obj, a_class):
        return True
    return False
