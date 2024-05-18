#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute 'size',
getter and setter for 'size', methods to calculate the square's area,
and a method to print the square using the character '#'.
"""

class Square:
    """
    Defines a square by a private instance attribute 'size' with getter and setter,
    and includes a method to calculate the area and a method to print the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size, defaulting to 0.

        Args:
            size (int): The side length of the square.
        """
        self.size = size  # This uses the setter to enforce type and value constraints

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
        Set the size of the square, ensuring the value is an integer and non-negative.

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

    def my_print(self):
        """
        Print the square with the character '#'. If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
