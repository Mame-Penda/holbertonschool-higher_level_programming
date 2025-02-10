#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""
import sys
from _5_save_to_json_file import save_to_json_file
from _6_load_from_json_file import load_from_json_file


try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
