#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    b = 0
    for e in my_list:
        if e > b:
            b = e
    return b
