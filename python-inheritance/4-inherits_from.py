#!/usr/bin/python3
"""
This module defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is instance of class inherited from specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is an instance of a subclass.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
