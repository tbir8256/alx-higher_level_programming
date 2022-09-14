#!/usr/bin/python3
"""A square class"""


class Square:
    """Drives a square."""
    def __init__(self, size=0):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise valueError("size must be >= 0")
    self.__size = size

    def area(self):
    """Calculates the area of a square
    Returns: the area of the square"""

    return (self.__size ** 2)

@property
def size(self):
    """Retrieves the value of `size`"""
    return self.__size

@size.setter
def size(self, value):
    """Sets the value of `value`"""
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if (value < 0):
        raise ValueError("size must be >= 0")

    self.__size = value

    def my_print(self):
        """Prints a square to stdout using #"""
        if self.__size == 0:
            print()

            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                    print()
