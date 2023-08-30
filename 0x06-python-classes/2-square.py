#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    A class that defines a square by its size
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance with an optional size
        Args:
            size (int, optional): The size of the square (default is 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
