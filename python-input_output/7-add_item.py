#!/usr/bin/python3
"""
mod 7

Uses:
- 'save_to_json_file' to save the list to a file.
- 'load_from_json_file' to load the existing list from the file.

The script does not handle file permission exceptions or check for the validity of JSON content.
"""

def load_from_json_file(filename):
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_to_json_file(my_obj, filename):
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

import sys
import os

def main():
    filename = "add_item.json"

    if os.path.exists(filename):
        from load_from_json_file import load_from_json_file
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])

    from save_to_json_file import save_to_json_file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
