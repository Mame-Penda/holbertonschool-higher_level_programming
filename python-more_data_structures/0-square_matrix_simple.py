#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix (list of lists): A 2D array of integers.

    Returns:
        list of lists: A new matrix with squared values, same size as the input matrix.
    """
    # Utiliser une compréhension de liste pour créer une nouvelle matrice avec les carrés des valeurs
    return [[x ** 2 for x in row] for row in matrix]
