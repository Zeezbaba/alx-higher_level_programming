#!/usr/bin/python3
#square class by Zeezbaba

class Square:
    """Initializing square class"""
    def __init__(self, size = 0):
        self.__size = size
"""size must be an integer.
    if size is not an integer, raise a typeerror"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
    """if size is less than zero, raise a valueerror"""
        if size < 0:
            raise ValueError("size must be >= 0")
