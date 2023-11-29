#!/usr/bin/python3
for l in range(25, -1, -1):
    h = l + ord('A')
    if l % 2 == 1:
        h += 32
        print('{:c}'.format(h), end='')
