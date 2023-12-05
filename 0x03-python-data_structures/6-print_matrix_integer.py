#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for q in matrix:
        c = 0
        for e in q:
            c += 1
            print('{:d}'.format(e), end=(" " if c < len(q) else ""))
        print()
