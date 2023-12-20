#!/usr/bin/python3
def magic_calculation(a, b):
    n = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            n += a ** b / i
        except Exception:
            n = b + a
            break
    return (n)
