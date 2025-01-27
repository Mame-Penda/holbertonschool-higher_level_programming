#!/usr/bin/python3
class square:
    """Class qui définit un carré avec des méthodes sa taille, son aire."""
    def __init__(self, size=0):
        """Initialize instance square.

        Args:
        size (int): Size of square

        Raises:
        TypeError: if size is not integer.
        ValueError: if size is negative.
        """
        self.size = size

        @property
        def size(self):
            """ Recovered the size of square

            Returns:
            int: Size of actual square.
            """
            return self.__size

        @size.setter
        def size(self, value):
            """Define a size square after validation.

            Args:
            value (int): Nex size of square.

            Raises:
            TypeError: if value is not a integer.
            ValueError: if value is negatif
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


def area(self):
    """calcul and return area of square.

    Returns:
    int: Area of square.
    """
    return self.__size ** 2


def my_print(self):
    """Print a square with the character '#' in stdout.

    if the size is 0, a empty line is printed.
    """
    if self.__size == 0:
        print("")
    else:
        for _ in range(self.__self):
            print("#" * self.__size)
