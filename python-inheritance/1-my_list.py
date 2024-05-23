#!/usr/bin/python3
"""
module 1
"""


class MyList(list):
    """
    mylsit class
    """
    def print_sorted(self):
        """
        print func.
        """
        sorted_list = sorted(self)
        print(sorted_list)
