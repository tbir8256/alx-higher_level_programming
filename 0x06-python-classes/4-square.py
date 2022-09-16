#!/usr/bin/python3
"""A square class. """


class Square:
    """Drives a square. """

    def __init__(self, size=0):
        """Initializes the data

        Args:
            size (int): The size of the new square
            """
            self.size = size

            @property
            def size(self):
                """set the current size of the square."""
                return (self.__size)

            @size.setter
            def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
        """calculates the area of a square
        Returns: the area of the square"""

        return (self.__size ** 2)
