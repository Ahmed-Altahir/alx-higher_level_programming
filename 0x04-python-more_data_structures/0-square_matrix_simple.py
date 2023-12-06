#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for n in range(list(matrix)):
        new_matrix = list(map(lambda x: x**2, matrix[n]))

    return (new_matrix)
