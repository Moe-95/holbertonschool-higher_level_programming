#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from a specified class."""
    return isinstance(obj, a_class) and type(obj) != a_class
