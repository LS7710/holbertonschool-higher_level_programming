#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute size.
The size attribute is validated to ensure it's an integer and not negative.
"""


class Square:
    """
    Represents a square with methods to manage its size.

    Attributes:
        __size (int): size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance with a given size.

        Args:
            size (int): The size of a side of the square, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
