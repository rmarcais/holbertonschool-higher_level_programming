#!/usr/bin/python3
""" Module containing the function find_peak """


def find_peak_2(li, low, high, n):
    """ Function that returns a peak of a list of integers. """
    middle = int(low + (high - low) / 2)

    if (middle == 0 or li[middle] >= li[middle - 1]) and \
       (middle == n - 1 or li[middle] >= li[middle + 1]):
        return li[middle]

    elif middle > 0 and li[middle] < li[middle - 1]:
        return find_peak_2(li, low, middle - 1, n)

    else:
        return find_peak_2(li, middle + 1, high, n)


def find_peak(list_of_integers):
    """ Function that find a peak in a list of integers. """

    if list_of_integers is None or list_of_integers == []:
        return None

    ln = len(list_of_integers)

    return find_peak_2(list_of_integers, 0, ln - 1, ln)
