#!/usr/bin/python3
def no_c(my_string):
    newstr = my_string.translate({ord('c'): None})
    newstr = newstr.translate({ord('C'): None})
    return newstr
