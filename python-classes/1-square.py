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
    __init__(self, size)
        Initializes a new Square object with the specified size.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with the specified size.

        Parameters
        ----------
        size : int
            The size of the square.
        """
        self.__size = size
