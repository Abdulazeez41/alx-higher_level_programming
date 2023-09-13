#!/usr/bin/python3
"""
Write a string to text (UTF8) & return total of character written
"""


def write_file(filename="", text=""):
    """ module for write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
