#!/usr/bin/python3
""" 100-matrix_mul.py

Test file: 100-matrix_mul.txt

To test the function matrix_mul, run:
python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2


Function: matrix_mul
"""


def matrix_mul(m_a, m_b):
    """Function taht multiplies two matrices
    Args:
    m_a: Matrix A
    m_b: Matrix B
    Return:
    A new matrix
    """
    message1 = "m_a should contain only integers or floats"
    message2 = "m_b should contain only integers or floats"
    message3 = "each row of m_a must be of the same size"
    message4 = "each row of m_b must be of the same size"

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(isinstance(m_a[i], list) for i in range(len(m_a))) == 0:
        raise TypeError("m_a must be a list of lists")
    if any(isinstance(m_b[j], list) for j in range(len(m_b))) == 0:
        raise TypeError("m_b must be a list of lists")
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if isinstance(element, (int, float)) == 0:
                raise TypeError(message1)
    for row in m_b:
        for element in row:
            if isinstance(element, (int, float)) == 0:
                raise TypeError(message2)
    for i in range(len(m_a)):
        if i != 0:
            if len(m_a[i]) != len(m_a[i - 1]):
                raise TypeError(message3)
    for i in range(len(m_b)):
        if i != 0:
            if len(m_b[i]) != len(m_b[i - 1]):
                raise TypeError(message4)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new[i][j] += m_a[i][k] * m_b[k][j]
    return new
