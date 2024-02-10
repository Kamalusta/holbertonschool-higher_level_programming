#!/usr/bin/python3
''' creates an obj form json file'''
import json


def load_from_json_file(filename):
    ''' creates an obj form json file'''
    with open(filename, encoding="UTF-8") as fjson:
        return json.load(fjson)
