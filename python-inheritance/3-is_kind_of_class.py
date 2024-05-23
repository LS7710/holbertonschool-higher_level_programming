#!/usr/bin/python3
"""
module defines the is_kind_of_class function that checks if an object is an
instance of specified class or class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if object is instance of class
    that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to match against the object's type.

    Returns:
        bool: True if object is instance of, or if it is instance of class
        that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
