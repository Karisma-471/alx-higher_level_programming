#!/usr/bin/python3
"""A module that appends a file"""

def append_write(filename="", text=""):
    """A function that opens and append"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
