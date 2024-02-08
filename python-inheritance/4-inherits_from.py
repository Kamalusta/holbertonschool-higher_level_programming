#!/usr/bin/python3
'''
checks for inherited
'''


def inherits_from(obj, a_class):
    ''' checks for inherited '''
    if (type(obj) is not a_class):
        return issubclass(type(obj), a_class)
    else:
        return False
