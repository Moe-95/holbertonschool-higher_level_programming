#!/usr/bin/python3
"""
Load, add, save module
"""

import sys
import os.path


if __name__ == "__main__":
    from add_item import add_item

    filename = "add_item.json"

    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    args = sys.argv[1:]
    for arg in args:
        my_list.append(arg)

    save_to_json_file(my_list, filename)
