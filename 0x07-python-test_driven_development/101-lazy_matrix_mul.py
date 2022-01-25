#!/usr/bin/python3
"""101-lazy_matrix_mul.py

Test file: 101-lazy_matrix_mul.txt

To test the function lazy matrix_divided, run:
python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt


Function: lazy_matrix_mul
"""


import numpy
"""import the module NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices by using the module NumPy
    Args:
    m_a: Matrix A
    m_b: Matrix B
    Return:
    A new matrix
    """
    return numpy.matmul(m_a, m_b)
