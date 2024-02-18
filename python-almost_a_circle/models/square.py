#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, id."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """Return the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value
