#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """
    extends the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the elements of the list.
        """
        print(sorted(self))
