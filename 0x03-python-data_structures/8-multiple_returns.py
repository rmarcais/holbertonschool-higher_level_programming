#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        a = 0
        b = None
    else:
        a = len(sentence)
        b = sentence[0]
    newtuple = a, b
    return newtuple
