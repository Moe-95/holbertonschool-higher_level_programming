#!/usr/bin/python3
"""Module for Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize the square with size."""
        super().__init__(size, size)
        self.__size = size
