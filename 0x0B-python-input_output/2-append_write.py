#!/usr/bin/python3
"""append_wrtie"""


def append_write(filename="", text=""):
    """"filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
