#!/usr/bin/python3
"""
module 1.
"""


def write_file(filename="", text=""):
    """
    Writes string to text file and returns number of characters.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written.
    """


    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
