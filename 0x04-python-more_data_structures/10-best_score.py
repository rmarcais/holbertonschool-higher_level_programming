#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max_value = max(a_dictionary, key= lambda x: a_dictionary[x])
    return max_value
