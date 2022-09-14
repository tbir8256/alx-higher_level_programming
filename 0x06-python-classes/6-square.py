#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
    """Sets the value of `size`"""
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if (value < 0):
        raise ValueError("size must be >= 0")
    self.__size = value
    @property
    def position(self):
    """Retrieves `position` value """
    return self.__position
@position.setter
def position(self, value):
    """Sets the value of `position`"""
    if not isinstance(value, tuple):
        raise TypeError("position must be a tuple of 2 positive integers")
    if len(value) != 2 or not all(isinstance(v, int) for v in value):
        raise TypeError("position must be a tuple of 2 positive integers")
    if not all(num >= 0 for num in value):
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value
    def my_print(self):
        """Prints a square to stdout using #"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(self.position[1])]
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                    print()
