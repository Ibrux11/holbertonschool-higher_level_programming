#!/usr/bin/python3
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    for num in list[1:]:
        if num > result:
            result = num
    return result