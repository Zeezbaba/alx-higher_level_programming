#!/usr/bin/python3
""" that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """ function that returns the dictionary
    description with simple data structure
    """
    return obj.__dict__
