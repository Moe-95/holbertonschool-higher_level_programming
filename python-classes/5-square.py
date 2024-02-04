#!/usr/bin/python3
"""5-square module"""


class Square:
    """Square class with private size attribute"""
    def __init__(self, size=0):
        """Initialize the Square instance with a size"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
