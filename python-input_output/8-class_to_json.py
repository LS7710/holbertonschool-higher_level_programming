#!/usr/bin/python3
"""
module 8
"""


def class_to_json(obj):
    """
    Returns

    Args:
        obj: An instance of a Class whose attributes are serializable.

    Returns:
        A dictionary containing all serializable attributes of obj.
    """
    return obj.__dict__
