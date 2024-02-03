#!/usr/bin/python3
'''bla bla bla'''


class Square:
    '''bla bla bla'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if all(isinstance(v, int) and v > 0 for v in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
