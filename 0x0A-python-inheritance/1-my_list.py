#!/usr/bin/python3
"""A MyList class that inherits a list"""


class MyList(list):
    """My list class that inherits list"""
    def print_sorted(self):
        """Method that prints a sorted list"""
        print(sorted(self))
