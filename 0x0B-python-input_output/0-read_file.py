#!/usr/bin/python3
"""read_file method"""


def read_file(filename=""):
    """prints stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
