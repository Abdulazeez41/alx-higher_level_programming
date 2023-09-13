#!/usr/bin/python3
'''A script that adds all arguments to a Python list, and then save them to a file
'''
import json


def save_to_json_file(my_obj, filename):
    ''' module save_to_json_file
    Recieve Python object and sends JSON representation to file
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
