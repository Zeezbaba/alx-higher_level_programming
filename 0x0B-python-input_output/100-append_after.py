#!/usr/bin/python3
"""Module that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as written:
        written.write(text)
