#!/usr/bin/python3
"""
This module contains the MagicClass class
"""

import math


class MagicClass:
    """
    A class that replicates the provided bytecode behavior
    """
    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance
        Args:
            radius (int or float, optional): The radius of the circle (default is 0)
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle
        Returns:
            float: The area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle
        Returns:
            float: The circumference of the circle
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    my_circle = MagicClass(5)
    print(my_circle.area())
    print(my_circle.circumference())
