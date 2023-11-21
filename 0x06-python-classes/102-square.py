#!/usr/bin/python3
"""The square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Initializes a Square
        Args: size: length of sides of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The property of size as the side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Derive the area of a Square
        Returns: The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
