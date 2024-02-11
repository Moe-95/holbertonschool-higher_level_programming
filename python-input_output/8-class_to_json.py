#!/usr/bin/python3

def class_to_json(obj):
    """Return the dictionary description of the given object for JSON serialization."""
    return obj.__dict__

if __name__ == "__main__":
    class MyClass:
        def __init__(self, name):
            self.name = name
            self.number = 0

    m = MyClass("John")
    m.number = 89
    print(class_to_json(m))
