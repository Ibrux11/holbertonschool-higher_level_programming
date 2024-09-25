#!/usr/bin/python3
    
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Parameters:
    obj: Any type
    The object to be checked.
    a_class: type
    The class to compare the object against.

    Returns:
    bool
    True if the object is exactly an instance of a_class,
    otherwise False.

    Example:
    >>> is_same_class(1, int)
    True
    >>> is_same_class(1, float)
    False
    >>> is_same_class(1, object)
    False
    """

    return type(obj) is a_class
