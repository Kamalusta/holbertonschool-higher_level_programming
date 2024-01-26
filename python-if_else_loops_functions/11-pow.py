#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1/a
        b *= -1
    scr = a
    for i in range(1, b):
        scr *= a
    return scr
