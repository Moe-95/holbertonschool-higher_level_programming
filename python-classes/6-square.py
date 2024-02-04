#!/usr/bin/python3
"""6-square module"""


class Square:
    """Square class with private size and position attributes"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance with a size and position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position attribute"""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(i, int) for i in value) \
           or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
