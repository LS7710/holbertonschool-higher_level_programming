#!/usr/bin/python3
"""
Module 101-add_attribute
"""


def add_attribute(obj, attr_name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which to add the attribute.
        attr_name (str): The name of the attribute to add.
        value: The value to set the attribute to.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
