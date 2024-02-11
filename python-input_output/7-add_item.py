#!/usr/bin/python3
"""
Adds all arguments to a Python list and then saves them to a file
"""

import sys
import os.path
from json import dump, load


if __name__ == "__main__":
    # File to save the list
    filename = "add_item.json"

    # Initialize an empty list
    my_list = []

    # Check if the file exists and load its content if it does
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            my_list = load(file)

    # Add command line arguments to the list
    for arg in sys.argv[1:]:
        my_list.append(arg)

    # Save the list as a JSON representation
    with open(filename, mode='w', encoding='utf-8') as file:
        dump(my_list, file)
