#!/usr/bin/python3
"""Defines a class square."""
class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes a new square object.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size value.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size value of the square object."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the object"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a # square per the size value"""
        for n in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
