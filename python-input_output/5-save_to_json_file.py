#!/usr/bin/python3
"""
module 5
"""


import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to file.

    Args:
        my_obj: The Python object to serialize.
        filename (str): filename.

    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
