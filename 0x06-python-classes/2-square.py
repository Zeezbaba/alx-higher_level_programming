#!/usr/bin/python3
# square class by Zeezbaba
"""Defines a square"""


class Square:
    """square class"""

    def __init__(self, size = 0):
        """Initializes a square class"""

        self.__size = size

    """size must be an integer.
    if size is not an integer, raise a typeerror
    if size is less than zero, raise a Valueerror
    """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
