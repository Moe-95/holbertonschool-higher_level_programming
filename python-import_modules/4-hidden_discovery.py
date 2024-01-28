#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    attributes = dir(hidden_4)

    sorted_attributes = sorted(attributes)

    for attr in sorted_attributes:
        if not attr.startswith("__"):
            print(attr)
