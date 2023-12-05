#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A child square class"""

    def __init__(self, size):
        """Initialize a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
