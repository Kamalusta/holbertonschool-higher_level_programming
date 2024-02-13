#!/usr/bin/python3
'''
this is base class. it will count instances
'''
import json


class Base:
    '''this is base class. it will count instances'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''data to JSON'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save the data to json file'''
        mylist = []
        if list_objs is None:
            return "[]"
        else:
            for i in list_objs:
                mylist.append(i.to_dictionary())
        with open(f"{cls.__name__}.json", 'w', encoding="UTF-8") as wfile:
            wfile.write(Base.to_json_string(mylist))
