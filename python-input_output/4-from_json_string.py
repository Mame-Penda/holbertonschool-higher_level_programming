#!/usr/bin/python3
"""Defines for from string-to-JSON function."""
import json


def from_json_string(my_str):
    """returns the python object representation of a JSON string."""
    return json.loads(my_str)
