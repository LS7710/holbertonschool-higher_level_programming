#!/usr/bin/python3
"""
This module provides a function 'say_my_name' that prints a person's full name.
It is designed to demonstrate basic Python functionality and error handling.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a name in the format "My name is <first name> <last name>".

    Args:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person. Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name are not strings.

    Returns:
    None: This function prints to stdout and does not return a value.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}".strip())
