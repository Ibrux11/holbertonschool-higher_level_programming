#!/usr/bin/python3
"""
This module defines a Square class.
"""

class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    __size : int
        The size of the square (private attribute).

    Methods
    -------
    __init__(self, size=0)
        Initializes a new Square object with the specified size.
    area(self)
        Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object with the specified size.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2
