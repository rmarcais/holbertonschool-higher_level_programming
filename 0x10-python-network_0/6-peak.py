#!/usr/bin/python3
""" Module containing the function find_peak """


def find_peak(list_of_integers):
    """ Function that find a peak in a list of integers. """

    if list_of_integers == [] or list_of_integers is None:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if list_of_integers[int(len(list_of_integers)
                            / 2)] <= list_of_integers[int(len(list_of_integers)
                                                          / 2 - 1)]:
        return(find_peak(list_of_integers[0:int(len(list_of_integers) / 2)]))
    else:
        return(find_peak(list_of_integers[
            int(len(list_of_integers)
                / 2):int(len(list_of_integers))]))
