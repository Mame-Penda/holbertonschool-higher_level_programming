#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix (list of lists): A 2D array of integers.

    Returns:
    """
    return [[x ** 2 for x in row] for row in matrix]
