#!/usr/bin/python3
''' writes an object to a file as json'''
import json


def save_to_json_file(my_obj, filename):
    ''' writes an object to a file as json'''
    with open(filename, 'w', encoding="UTF-8") as write:
        json.dump(my_obj, write)
