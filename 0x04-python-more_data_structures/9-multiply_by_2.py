#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for x, y in a_dictionary.items():
        y = y * 2
        new[x] = y
    return new
