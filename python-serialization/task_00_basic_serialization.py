#!/usr/bin/python3
"""
mod 0
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the provided dictionary and save it to the specified file.

    Parameters:
    data (dict): The dictionary to be serialized.
    filename (str): The name of the file to save the JSON data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load JSON data from the specified file, deserialize to dictionary.

    Parameters:
    filename (str): The name of the file to load the JSON data from.
    Returns:

    dict: The deserialized dictionary from the JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
