#!/usr/bin/python3
# 6-square.py
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): Position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size value of the square object."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance (value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance (value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the object"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a # square according to the size value"""
        if self.__size == 0:
            print("")
            return

        [print ("") for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
