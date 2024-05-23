#!/usr/bin/python3
"""
This module defines the BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry class for geometric operations with added integer validation.
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
            Exception: Indicates that the method needs to be implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
