#!/usr/bin/python3
"""
This module defines the is_same_class function that checks if an object is
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to match the type of the object.

    Returns:
        bool: True if the object is instance of the class, False otherwise.
    """
    return type(obj) is a_class
