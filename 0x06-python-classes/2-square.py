#!/usr/bin/python3
# 2-square.py
"""Defines a class square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square object.

        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
