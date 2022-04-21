#!/usr/bin/python3
""" Module containing the function find_peak """


def find_peak(list_of_integers):
    """ Function that find a peak in a list of integers. """

    if list_of_integers == [] or list_of_integers is None:
        return None

    li = list_of_integers
    ln = len(li)

    if ln == 1:
        return li[0]

    if li[int(ln / 2)] <= li[int(ln / 2 - 1)]:
        return(find_peak(li[0:int(ln / 2)]))
    else:
        return(find_peak(li[int(ln / 2):int(ln)]))
