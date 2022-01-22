#!/usr/bin/python3
"""2-matrix_divided.py

Test file: 2-matrix_divided.txt

To tesy the function matrix_divided, run:
python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2

Function: matrix_divided
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.
    Args:
    matrix: the matrix to divide
    div: the divider
    Return:
    A new matrix
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = matrix[i].copy()
        if i != 0:
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError(message2)
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], (int, float)) == 0:
                raise TypeError(message1)
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
