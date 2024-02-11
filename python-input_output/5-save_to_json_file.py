#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Write the JSON representation of the given object to the specified file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

if __name__ == "__main__":
    my_list = [1, 2, 3]
    save_to_json_file(my_list, "my_list.json")
