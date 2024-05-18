#!/usr/bin/python3
"""
This module defines a Square class with private instance attribute 'size'
with its getter and setter, and a method to calculate the area of the square.
The setter method includes checks for the value type and value constraints.
"""

class Square:
    """
    A class that defines a square by a private instance attribute 'size' and
    provides a method to calculate the area of the square. The size attribute
    has a getter and setter to ensure the value is an integer and non-negative.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size, defaulting to 0.
        
        Args:
            size (int): The side length of the square.
        """
        self.size = size  # this uses the size setter method

    @property
    def size(self):
        """
        Retrieve the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square, with checks for integer type and
        non-negative value.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
