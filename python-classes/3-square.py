#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):  # Check if size is an integer
            raise TypeError("size must be an integer")
        if size < 0:  # Check if size is non-negative
            raise ValueError("size must be >= 0")
        self.__size = size  # Define the private attribute

    def area(self):
        return self.__size ** 2  # Calculate the area
