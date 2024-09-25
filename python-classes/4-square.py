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
    size(self)
        Gets the current size of the square.
    size(self, value)
        Sets the size of the square.
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
        self.size = size
    
    @property
    def size(self):
        """
        Gets the current size of the square.

        Returns
        -------
        int
            The current size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters
        ----------
        value : int
            The new size of the square.

        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size * self.__size
