#!/usr/bin/python3
"""
module 6
"""


import json

def load_from_json_file(filename):
    """
    Creates obj.

    Args:
        filename (str): The name of the file

    Returns:
        object: obj.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
