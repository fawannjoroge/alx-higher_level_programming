#!/usr/bin/env python3
def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string."""
    newStr = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            newStr += letter
    return newStr
