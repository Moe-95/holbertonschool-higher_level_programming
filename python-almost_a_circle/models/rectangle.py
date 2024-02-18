from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance with width, height, x, y, id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Assign arguments to attributes."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Print in stdout the Rectangle instance with the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
