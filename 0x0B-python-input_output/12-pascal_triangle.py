#!/usr/bin/python3
"""12-pascal_triangle.py
Module containing the function pascal_triangle.
"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """

    if n <= 0:
        return []

    tgl = [[]]
    a = 0

    for i in range(n):
        add1 = 0
        add2 = 0
        tgl[i].append(1)
        if i >= 2:
            for j in range(a):
                tgl[i].append(tgl[i - 1][add1] + tgl[i - 1][add2 + 1])
                add1 += 1
                add2 += 1
        if i != n - 1:
            tgl.append([])
        if i >= 1:
            tgl[i].append(1)
            a += 1
    return tgl
