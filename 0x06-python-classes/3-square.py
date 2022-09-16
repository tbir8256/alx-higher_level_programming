#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Derives a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int):Size of the square.
            """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

    def area(self):
        """Calculates the area
        Returns:
            current area of the square.
            """
        return (self.__size ** 2)
