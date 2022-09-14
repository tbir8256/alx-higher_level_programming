#!/usr/bin/python3
class Square:
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    self.__size = size
    def area(self):
    """calculates the area of a square
    Returns: the area of the square"""
    return (self.__size ** 2)
@property
def size(self):
    """Retrieves the value of `size`"""
    return self.__size
@size.setter
def size(self, value):
    """Sets the value of 'value'"""
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if (value < 0):
        raise ValueError("size must be >= 0")
    self.__size = value
