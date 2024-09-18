#!/usr/bin/python3
"""Define a class Square"""
class Square:
    def __init__(self, size=0):
        """Initializies a new object with th specified size
        Args:
            size: Size of the object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """Check a condition and if it is not checked it returns a
            differend erroro message for each condition.
        """
        self.__size =size