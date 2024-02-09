#!/usr/bin/python3
''' file writer'''


def write_file(filename="", text=""):
    ''' file writer'''
    count = 0
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(text)
        for i in text:
            count += 1
        return count
