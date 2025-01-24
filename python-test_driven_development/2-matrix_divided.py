#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix.
The function ensures that all rows of the matrix are of the same size
and that division is performed element-wise.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of (int or float)): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the divided values rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if rows of the matrix are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if matrix is None:
        raise TypeError("'NoneType' object is not iterable")
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
