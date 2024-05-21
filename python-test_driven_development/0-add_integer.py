#!/usr/bin/python3
"""
adds the add_integer function that adds two numbers.
"""

def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.
    Parameters:
    a (int, float): The first number to add.
    b (int, float, optional): The second number to add. Defaults to 98.

    If a or b are floats, they are converted to integers before addition.
    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
