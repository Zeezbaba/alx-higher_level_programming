#!/usr/bin/python3
"""A base geometry class"""


class BaseGeometry:
    """class that represent base geometry"""

    def area(self):
        """Area not inplemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
