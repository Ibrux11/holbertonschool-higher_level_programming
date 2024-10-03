#!/usr/bin/python3
"""
Module to demonstration serialization
"""


def to_json_string(my_obj):
    """
    Function that returns the JSON representation 
    of an object (string)
    """

    import json


    json_data = json.dumps(my_obj)
    return json_data
