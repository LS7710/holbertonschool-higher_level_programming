#!/usr/bin/python3
"""
This module defines the lookup function that returns a list of attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of `obj`.

    Args:
        obj (object): The object to list attributes and methods for.

    Returns:
        list: A list of strings containing the names of the object's attributes.
    """
    return dir(obj)
