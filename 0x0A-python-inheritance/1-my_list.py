#!/usr/bin/python3
"""
    A module that inherit list from a parent class
"""


class MyList(list):
    """A child class to parent class list"""
    def print_sorted(self):
        """to print sorted list"""
        print(sorted(self))
