#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in matrix[i]:
            if matrix[i].index(j) != 0:
                print(' ', end='')
            print("{:d}".format(j), end='')
        print()
