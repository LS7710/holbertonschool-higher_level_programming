#!/usr/bin/python3
"""
module 4.
"""
import json


def from_json_string(my_str):
    """
    Returns object.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: data structure represented by string.
    """

    return json.loads(my_str)
