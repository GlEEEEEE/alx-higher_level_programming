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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        Args:
            value (int): The size value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2
