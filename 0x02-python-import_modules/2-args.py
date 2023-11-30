#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    cunt = len(sys.argv)

    if (cunt == 0):
        print("0 arguments.")
    elif (cunt == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(cunt))
        number = 1
        for argument in sys.argv:
            print("{:d}: {}".format(number, argument))
            number += 1
