#!/usr/bin/python3
"""
Module 1
"""


class MyList(list):
    """
    inherits fro list.
    """
    def print_sorted(self):
        """
        Prints ascending.
        """
        sorted_list = sorted(self)
        print(sorted_list)
