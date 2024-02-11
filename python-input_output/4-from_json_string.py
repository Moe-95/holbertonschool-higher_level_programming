#!/usr/bin/python3
import json

def from_json_string(my_str):
    """Return the Python data structure represented by the given JSON string."""
    return json.loads(my_str)

if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
