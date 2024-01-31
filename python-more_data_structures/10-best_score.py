#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None
    best = 0
    key = ''
    for k, v in a_dictionary.items():
        if best < v:
            best = v
            key = k
    return key
