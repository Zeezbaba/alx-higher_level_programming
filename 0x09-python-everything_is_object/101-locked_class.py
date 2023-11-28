#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    this module restrict user from creating new attributes aside "first_name"
    """

    __slots__ = ["first_name"]
