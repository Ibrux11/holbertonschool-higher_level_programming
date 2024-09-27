#!/usr/bin/python3
"""
Module defining a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the square description.

        Returns:
            str: The square description in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
