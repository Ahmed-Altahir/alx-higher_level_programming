#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nm = matrix.copy()

    for n in range(list(matrix)):
        nm = list(map(lambda x: x**2, matrix[n]))

    return (nm)
