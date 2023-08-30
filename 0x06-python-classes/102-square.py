#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance
        Args:
            size (int or float, optional): The size of the square's sides (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square's sides
        Returns:
            int or float: The size of the square's sides
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides
        Args:
            value (int or float): The size of the square's sides
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square
        Returns:
            int or float: The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two Square instances based on their area
        Args:
            other (Square): The other Square instance to compare
        Returns:
            bool: True if both Square instances have the same area, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two Square instances based on their area
        Args:
            other (Square): The other Square instance to compare
        Returns:
            bool: True if both Square instances do not have the same area, False otherwise
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two Square instances based on their area
        Args:
            other (Square): The other Square instance to compare
        Returns:
            bool: True if this Square's area is less than the other's, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two Square instances based on their area
        Args:
            other (Square): The other Square instance to compare
        Returns:
            bool: True if this Square's area is less than or equal to the other's, False otherwise
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two Square instances based on their area
        Args:
            other (Square): The other Square instance to compare
        Returns:
            bool: True if this Square's area is greater than the other's, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two Square instances based on their area
        Args:
            other (Square): The other Square instance to compare
        Returns:
            bool: True if this Square's area is greater than or equal to the other's, False otherwise
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_2 = Square(4)
    print(my_square_1 < my_square_2)
    print(my_square_1 <= my_square_2)
    print(my_square_1 > my_square_2)
    print(my_square_1 >= my_square_2)
    print(my_square_1 == my_square_2)
    print(my_square_1 != my_square_2)
