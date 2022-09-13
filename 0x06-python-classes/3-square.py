#!/usr/bin/python3
# 3-square.py
"""Defines a class square."""


class Square:
    """Represents a square defined by its size"""

    def __init__(self, size=0):
        """Initializes the square object.

        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the object
        """
        return (self.__size * self.__size)
