#!/usr/bin/python3
"""
module 7
"""

import sys
import os.path


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    filename = "add_item.json"
    try:
        if os.path.exists(filename):
            items = load_from_json_file(filename)
        else:
            items = []
    except FileNotFoundError:

        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
