#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for q in range(count):
        print("{}: {}".format(q + 1, sys.argv[q + 1]))
