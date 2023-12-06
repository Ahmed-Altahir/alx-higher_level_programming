#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    t = []
    for n in matrix:
        t.append(list(map(lambda n: n**2, n)))
    return (t)
