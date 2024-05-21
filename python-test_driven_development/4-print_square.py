#!/usr/bin/python3
"""
This module provides a function print_square that prints a square with the '#' character.
The function ensures that the input size is valid, enforcing integer and non-negative values.
"""

def print_square(size):
    """
    Prints a square with the character '#' based on the given size.

    Args:
    size (int): The length of the sides of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
