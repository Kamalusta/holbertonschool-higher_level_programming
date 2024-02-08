#!/usr/bin/python3
'''
slzjfn
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[{Square.__base__.__name__}] {self.__size}/{self.__size}"
