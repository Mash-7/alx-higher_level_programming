#!/usr/bin/python3
# 6-square.py
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(sef, siz=0, position=(0, 0)):
        """Initializes a new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the current size of the square."""
        return (self.__size)

    @size.setter
    def size(size, value):
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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int)
