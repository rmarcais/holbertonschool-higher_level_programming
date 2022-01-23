#!/usr/bin/python3
"""5-text_indentation.py

Test file: 5-text_indentation.txt

To test the function text_indentation, run:
python3 -m doctest -v ./tests/5-text_indentation.txt


Function:
text_indentation
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after each of these characters:., ? and :
    Args:
    text: The text to print
    Return:
    Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if len(text) == 0:
        return
    a = 0
    while text[a] == " ":
        if a != len(text) - 1:
            a += 1
        else:
            return
    b = len(text) - 1
    while text[b] == " ":
        b -= 1
    while a <= b:
        if text[a] in [".", ":", "?", "\n"]:
            print("{}".format(text[a]), end="")
            if text[a] != "\n":
                print()
                print()
                while a < b and text[a + 1] == " ":
                    if a != b - 1:
                        a += 1
                    else:
                        return
        else:
            print("{}".format(text[a]), end="")
        a += 1
