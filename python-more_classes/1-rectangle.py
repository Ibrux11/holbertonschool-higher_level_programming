#!/usr/bin/python3
class Rectangle:
    """
    A class to represent a rectangle.
    
    Attributes:
    -----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        
        Parameters:
        -----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        
        Returns:
        --------
        int
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        
        Parameters:
        -----------
        value : int
            The new width of the rectangle.
        
        Raises:
        -------
        TypeError:
            If the value is not an integer.
        ValueError:
            If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        
        Returns:
        --------
        int
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        
        Parameters:
        -----------
        value : int
            The new height of the rectangle.
        
        Raises:
        -------
        TypeError:
            If the value is not an integer.
        ValueError:
            If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value