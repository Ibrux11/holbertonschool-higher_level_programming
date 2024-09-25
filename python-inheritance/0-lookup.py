#!/usr/bin/python3

def lookup(obj):
    """
    Method to return a list of avaible attributes and methodes fo an object 
    :param obj : object that an availble atributes and methods
    :Return: a list"""
    return dir(obj)
