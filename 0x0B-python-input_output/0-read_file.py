#!/usr/bin/python3
"""
Rads a text file
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
