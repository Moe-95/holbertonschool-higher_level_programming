#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Read the JSON file and return the Python object it represents."""
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    my_list = load_from_json_file("my_list.json")
    print(my_list)
