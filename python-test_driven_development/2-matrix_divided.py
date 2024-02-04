#!/usr/bin/python3

"""
this module devide
all matrix elements
"""

def matrix_divided(matrix, div):
    """
    this function takes a matrix and a divider
    """
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                row.append(round(j / div, 2))
        new_matrix.append(row)
    return new_matrix
   
    
