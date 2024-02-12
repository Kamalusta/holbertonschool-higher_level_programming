#!/usr/bin/python3
'''
this is base class. it will count instances
'''


class Base:
    '''this is base class. it will count instances'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
