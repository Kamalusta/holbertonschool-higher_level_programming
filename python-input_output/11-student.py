#!/usr/bin/python3
''' doc '''


class Student():
    ''' doc '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        result = {}
        for i in attrs:
            for k, v in self.__dict__.items():
                if k == i:
                    result[k] = v
                    break
        return result

    def reload_from_json(self, json):
        if not json:
            return
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
