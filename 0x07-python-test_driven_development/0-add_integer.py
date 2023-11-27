#!/usr/bin/python3
"""This module defines an integer addition function"""


def add_integer(a, b=98):
    """Returns the addition of two integers or float as integers.

    Args:
        a: first arguments
        b: second arguments

    Returns:
        Sum of two arguments

    Raises:
        TypeError: If either of a or b is non integer or non float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
