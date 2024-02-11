#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """Return the JSON representation of the given object."""
    return json.dumps(my_obj)

if __name__ == "__main__":
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
