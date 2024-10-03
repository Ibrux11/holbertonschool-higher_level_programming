#!/usr/bin/python3
"""
Module to demonstration serialization
"""


def from_json_string(my_str):
    """ 
    Function that returns and object (Python data structure) 
    represented by a JSON string.
    """
    import json

    python_data = json.loads(my_str)
    return python_data