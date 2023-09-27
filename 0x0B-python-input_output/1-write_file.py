#!/usr/bin/python3
"""A module that writes into a file"""

def write_file(filename="", text=""):
    """A function that writes into a file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
