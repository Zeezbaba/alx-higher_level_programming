#!/usr/bin/python3
"""A rectangle class that inherit from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A child class Rectangle"""

    def __init__(self, width, height):
        """Initializes te rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
