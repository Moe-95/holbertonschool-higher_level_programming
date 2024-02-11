#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self) -> None:
        """Raise an exception if the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        """Validate the value as an integer and ensure it is greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
