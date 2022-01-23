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
    a = 0
    while a < len(text):
        if text[a] == "." or text[a] == "?" or text[a] == ":":
            print("{}".format(text[a]), end="")
            print()
            print()
            while a < len(text) and text[a + 1] == " ":
                a += 1
        else:
            print("{}".format(text[a]), end="")
        a += 1
