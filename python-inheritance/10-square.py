#!/usr/bin/python3
"""
Class for geometry operations.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, size):
        """Instantiation of size with validation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the rectangle.

        Uses the formula: size ** .
        """
        return self.__size ** 2

    
