#!/usr/bin/python3
"""Module for Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
