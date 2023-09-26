#!/usr/bin/python3
"""a module that opens and reads a file"""

def read_file(filename=""):
    """a function that read a file"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
