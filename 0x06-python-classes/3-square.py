#!/usr/bin/python3
"""A square class. """


class Square:
    """Derives a square. """
    def __init__(self, size=0):
        """Initializes the data. """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
        """Calculates the area of a square
        Returns: the area of the square"""

        return (self.__size ** 2)
