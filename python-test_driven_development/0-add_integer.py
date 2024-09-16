# 0-add_integer.py
def add_integer(a, b=98):
    """Function that adds two integers or floats.
    Args:
        a: First number, must be an integer or float.
        b: Second number, default is 98.
    Returns:
        The sum of a and b after casting them to integers.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
