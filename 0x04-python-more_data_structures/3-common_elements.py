#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for elements in set_1:
        for element in set_2:
            if elements == element:
                common.append(elements)
    return common
