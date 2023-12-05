#!/usr/bin/python3
"""A module that raises an exception message"""


class BaseGeometry:
    """A basegeometry class"""

    def area(self):
        """area is not implemented"""
        raise Exception("area() is not implemented")
