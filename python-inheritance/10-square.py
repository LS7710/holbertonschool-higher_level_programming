#!/usr/bin/python3
"""
Module 10-square
"""


Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """
    A class that represents a square, inherits from Rectangle.
    
    Attributes:
        __size (int): The size of the sides of the square, private attribute.
    """

    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (int): The size of the sides of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to zero.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return super().__str__()
