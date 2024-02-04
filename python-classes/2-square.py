#!/usr/bin/python3
"""2-square module"""


class Square:
    """Square class with private size attribute"""
    def __init__(self, size=0):
        """Initialize the Square instance with a size"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
