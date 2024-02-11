#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and not type(obj) is a_class
