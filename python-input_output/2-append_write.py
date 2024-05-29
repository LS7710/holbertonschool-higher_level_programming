#!/usr/bin/python3
"""
module 1.
"""


def append_write(filename="", text=""):
    """
    Appends string to end of a text file and returns the number of
    characters added.

    Args:
        filename (str): name of file being appended.
        text (str): string appended.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
