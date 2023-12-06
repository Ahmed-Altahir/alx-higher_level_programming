#!/usr/bin/python3
def multiple_by_2(a_dictionary):
    w = list(a_dictionary.key())

    for n in w:
        w[n] *= 2
    return (w)
