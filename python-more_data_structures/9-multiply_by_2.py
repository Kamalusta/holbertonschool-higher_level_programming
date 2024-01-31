#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}
    for k, v in a_dictionary.items():
        newdic[k] = v*2
    return newdic
