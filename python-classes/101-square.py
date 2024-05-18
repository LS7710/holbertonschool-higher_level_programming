#!/usr/bin/python3
"""
This module defines a Square class which encapsulates the properties
and methods of a square, with added functionalities to print the square
directly using print() and handle its position.
"""

class Square:
    """
    A class that defines a square by private instance attributes 'size' and
    'position' with respective getter and setter methods, includes methods
    to calculate the area, and print the square considering its position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size, defaulting to 0, and
        a position, defaulting to (0, 0).
        
        Args:
            size (int): The side length of the square.
            position (tuple): The (x, y) tuple indicating position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square, ensuring it is a tuple of 2 positive integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' considering its 'position'.
        """
        print(self.__str__())

    def __str__(self):
        """
        String representation of the square for printing.

        Returns:
            str: Formatted string based on the size and position of the square.
        """
        if self.__size == 0:
            return ""
        
        result = "\n" * self.__position[1]
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()
