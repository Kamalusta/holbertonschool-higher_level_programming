#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        arr = list(map(lambda a: a*a, matrix[i]))
        new_matrix.append(arr)
    return new_matrix
