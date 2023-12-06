#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.key())
    order.sort()
    for p in order:
        print("{:s}: {}".format(p, order[p]))
