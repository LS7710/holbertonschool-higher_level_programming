#!/usr/bin/python3
"""
This module provides the function text_indentation that processes text and formats it by inserting two new lines after each '.', '?', and ':'.
It ensures the text follows the specified formatting rules for educational purposes and clarity in text processing.
"""

def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?', or ':' character.

    Args:
    text (str): The text to format.

    Raises:
    TypeError: If the input text is not a string.

    Returns:
    None: This function prints to stdout and does not return a value.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        if char in '.?:':
            print("\n\n", end="")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
