#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            char = chr(ord(i)-32)
        else:
            char = i
        print("{}".format(char), end='')
    print()
