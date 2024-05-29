#!/usr/bin/python3
"""
module 7
"""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """
    this is here so it passes pep8, im tired.
    """
    filename = "add_item.json"

    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
