#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each of these characters: '.', '?', ':'

    Args:
        text (string): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":  # Check for the delimiters
            print("\n")
            # Skip any spaces after the delimiter
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
