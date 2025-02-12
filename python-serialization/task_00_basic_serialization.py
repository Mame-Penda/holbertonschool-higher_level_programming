#!/usr/bin/python3
"""Defines serialize_and_save_to_file and load_and_deserialize methods."""
import json


def serialize_and_save_to_file(data, filename):
    """serialize a python dictionary to a JSON file."""
    with open(filename, 'w+', encoding="utf-8") as f:
        data = json.dumps(data)
        f.write(data)
    pass


def load_and_deserialize(filename):
    """deserialize the JSON file to recreate the python Dinctionary."""
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)
    pass
