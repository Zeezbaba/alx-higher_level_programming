#!/usr/bin/python3
"""A base geometry class"""


class BaseGeometry:
    """class that represent base geometry"""

    def area(self):
        """Area not inplemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validates integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
