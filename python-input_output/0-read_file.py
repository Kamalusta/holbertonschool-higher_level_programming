#!/usr/bin/python3
def read_file(filename=""):
    ''' it reads files'''
    with open(filename, encoding='UTF-8') as file:
        print(file.read())
