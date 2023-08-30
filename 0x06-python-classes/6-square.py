#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    A class that defines a square by its size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with an optional size and position
        Args:
            size (int, optional): The size of the square (default is 0)
            position (tuple, optional): The position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square
        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square
        Args:
            value (tuple): The position value to be set
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate and return the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
