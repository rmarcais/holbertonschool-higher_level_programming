#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        letter = ord(letters)
        if letter < 123 and letter > 96:
            letter = letter - 32
        print("{}".format(chr(letter)), end="")
    print()
