#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key_, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key_, value))
