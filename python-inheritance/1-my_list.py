#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order without modifying the original list.
        
        :Return: None"""
        print(sorted(self))