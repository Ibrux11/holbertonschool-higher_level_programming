#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation of width and height with validation"""

        self.integer_validator("width", width)
        self.integer_validator("heigt", height)

        self.__width = width
        self.__height = height
