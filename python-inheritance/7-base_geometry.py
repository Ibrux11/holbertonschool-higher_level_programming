#!/usr/bin/python3
""""""


class BaseGeometry:
    """BaseGeometry class with public instance methods for area and integer validation."""
    
    def area(self):
        """Raises an Exception as area is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.

        Args:
            name (str): Name of the parameter.
            value (int): Value of the parameter to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
