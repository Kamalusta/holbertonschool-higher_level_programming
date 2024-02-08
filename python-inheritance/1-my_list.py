#!/usr/bin/python3
'''
this is sorted list class
'''


class MyList(list):
    ''' class inherits form list class'''
    def print_sorted(self):
        print(sorted(self))
