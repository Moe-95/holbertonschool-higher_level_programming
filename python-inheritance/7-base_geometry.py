#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raise an exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
