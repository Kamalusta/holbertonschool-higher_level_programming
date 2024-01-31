#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for i in roman_string:
        for k, v in romans.items():
            if i is k:
                res += v
                if v > prev:
                    res = res - (prev * 2)
                prev = v
    return res
