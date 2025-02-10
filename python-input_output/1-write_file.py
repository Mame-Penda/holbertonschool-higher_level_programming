#!/usr/bin/python3
"""Defines a text files-reading function."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8)."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
