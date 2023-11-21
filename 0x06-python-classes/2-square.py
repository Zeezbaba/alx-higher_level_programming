#!/usr/bin/python3
# 0-square.py by Zeezbaba
"""This module defines a square"""


class Square:
    """This class is representing a square"""

    def __init__(self, size = 0):
        """Initializes the square class
        Args:
            size: represent the size of the square given
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
