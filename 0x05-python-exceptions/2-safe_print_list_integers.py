#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0

    for u in range(x):
        try:
            print("{:d}".format(my_list[u]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            n += 1

    print()
    return (n)
