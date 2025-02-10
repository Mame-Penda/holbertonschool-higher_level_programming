#!/usr/bin/pytho3
"""Defines a string-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    return obj.__dict__
