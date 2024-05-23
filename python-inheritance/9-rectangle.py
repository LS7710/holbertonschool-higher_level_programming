#!/usr/bin/python3
"""
Module 9-rectangle
"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle, must be a positive integer.
        __height (int): The height of the rectangle, must positive integer.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with validated width and height.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the rectangle description.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
