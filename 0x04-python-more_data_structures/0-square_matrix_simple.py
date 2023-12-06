#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = []
    for n in matrix:
        tmp.append(list(map(lambda n: n**2, n)))
    return (tmp)
