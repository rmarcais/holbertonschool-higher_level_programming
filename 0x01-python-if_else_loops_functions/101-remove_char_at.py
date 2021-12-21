#!/usr/bin/python3
def remove_char_at(str, n):
    copystr2 = ""
    if n >= len(str) or n < 0:
        return str
    for i in range(0, n):
        copystr2 = copystr2 + str[i]
    for i in range(n + 1, len(str)):
        copystr2 = copystr2 + str[i]
    return copystr2
