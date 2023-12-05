#!/usr/bin/python3
"""Module that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Prints the content of the file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
