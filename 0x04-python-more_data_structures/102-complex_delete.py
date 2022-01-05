#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys in a_dictionary.copy():
        if a_dictionary[keys] == value:
            del a_dictionary[keys]
    return a_dictionary
