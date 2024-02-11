#!/usr/bin/python3
"""Module for Square class."""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.width}/{self.height}"

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize the square with size."""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.integer_validator("size", value)
        self.__size = value

    def integer_validator(self, name, value):
        """Validate the value as an integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
