#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(matrix):
        for j in range(matrix[i]):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (matrix[i] - 1):
                print(" ", end="")
                print("")
