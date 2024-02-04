#!/usr/bin/python3

"""
f*cing function
"""


def print_square(size):
    """
    calc square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
