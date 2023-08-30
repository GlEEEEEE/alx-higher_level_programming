#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance
        Args:
            size (int, optional): The size of the square's sides (default is 0)
            position (tuple, optional): The position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square's sides
        Returns:
            int: The size of the square's sides
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides
        Args:
            value (int): The size of the square's sides
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
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
            value (tuple): The position of the square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(coord, int) for coord in value) or
                not all(coord >= 0 for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)


if __name__ == "__main__":
    my_square = Square(3, (1, 1))
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.position = (2, 2)
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.position = (0, 0)
    my_square.my_print()
