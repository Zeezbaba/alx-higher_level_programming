#!/usr/bin/python3
"""

This module defines a text indentation function

"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string text to print

    Raises:
        TypeError: If text is not a string

    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = 0
    while formatted_text < len(text) and text[formatted_text] == " ":
        formatted_text = formatted_text + 1

    while formatted_text < len(text):
        print(text[formatted_text], end="")
        if text[formatted_text] == "\n" or text[formatted_text] in ".?:":
            if text[formatted_text] in ".?:":
                print("\n")
            formatted_text = formatted_text + 1
            while formatted_text < len(text) and text[formatted_text] == " ":
                formatted_text += 1
            continue
        formatted_text += 1
