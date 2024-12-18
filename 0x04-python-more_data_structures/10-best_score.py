#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    """
    if a_dictionary and len(a_dictionary):
        max_key = list(a_dictionary.keys())[0]
        for key in a_dictionary:
          if a_dictionary[key] > a_dictionary[max_key]:
              max_key = key
        return max_key
    return None
