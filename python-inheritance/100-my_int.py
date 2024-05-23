#!/usr/bin/python3
"""
Module 100-my_int
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted '==' and '!=' operators.
    """

    def __eq__(self, other):
        """
        Override the '==' operator to behave like '!='.
        """
        return super().__eq__(other) is False

    def __ne__(self, other):
        """
        Override the '!=' operator to behave like '=='.
        """
        return super().__eq__(other) is True
