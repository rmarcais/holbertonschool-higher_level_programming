#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    for element in range(len(my_list)):
        if my_list[element] == search:
            newlist[element] = replace
    return newlist
