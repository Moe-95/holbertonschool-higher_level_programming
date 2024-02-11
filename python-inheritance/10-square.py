class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize the square with size."""
        self.integer_validator("size", size)  # Validate the size
        super().__init__(size, size)
        self.__size = size
