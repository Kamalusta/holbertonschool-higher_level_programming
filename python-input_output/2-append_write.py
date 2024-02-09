#!/usr/bin/python3
'''append the text to a file'''


def append_write(filename="", text=""):
    '''append the text to a file'''
    with open(filename, 'a', encoding="UTF-8") as afile:
        afile.write(text)
        return len(text)
