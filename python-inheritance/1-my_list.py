#!/usr/bin/python3
"""
module defines the MyList class which inherits from list class and
adds a method to print list in ascending order.
"""


class MyList(list):
    """
    MyList class that inherits from list.

    Methods:
        print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
