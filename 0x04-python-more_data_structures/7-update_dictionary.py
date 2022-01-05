#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    t = 0
    for keys in a_dictionary:
        if keys == key:
            a_dictionary[keys] = value
            t = 1
    if t == 0:
        a_dictionary[key] = value
    return a_dictionary
