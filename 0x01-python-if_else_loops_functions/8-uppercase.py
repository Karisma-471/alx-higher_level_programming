#!/usr/bin/python3
def uppercase(input_str):
    """Print a string in uppercase."""
    for c in input_str:
        if 'a' <= c <= 'z':
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print("")
