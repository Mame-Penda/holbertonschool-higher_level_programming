#!/usr/bin/python3
class square:
    """Class qui définit un carré avec une taille validée."""
    def __init__(self, size=0):
        """Initialize square.

        Args:
        size (int): Size of square

        Raises:
        TypeError: if size is not integer.
        ValueError: if size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
