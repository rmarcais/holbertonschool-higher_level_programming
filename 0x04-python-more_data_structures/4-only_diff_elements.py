#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    t = 0
    diff = []
    for elements in set_1:
        for element in set_2:
            if elements == element:
                t = 1
        if t == 0:
            diff.append(elements)
        t = 0
    for element in set_2:
        for elements in set_1:
            if elements == element:
                t = 1
        if t == 0:
            diff.append(element)
        t = 0
    return diff
