#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check for lowercase letters
            c = chr(ord(c) - 32)  # Convert lowercase to uppercase
        print("{}".format(c), end="")  # Print each character
    print("")  # Print a newline at the end

