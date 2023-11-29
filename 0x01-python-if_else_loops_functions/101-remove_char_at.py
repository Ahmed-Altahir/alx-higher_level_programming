#!/usr/bin/python3

def remove_char_at(str, n):
    ns = ''
    for o, v in enumerate(str):
        if o != n:
            ns += v
            return ns
