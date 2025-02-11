#!/usr/bin/pytho3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    and returns number of characters appended."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
