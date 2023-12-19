#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        Args:
            size (int): The size of the new square.
        
        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError
        self.__size = size
