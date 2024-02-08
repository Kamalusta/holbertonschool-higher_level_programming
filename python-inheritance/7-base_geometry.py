#!/usr/bin/python3
'''
empty class
'''


class BaseGeometry:
    ''' empty '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        if name is None or value is None:
            raise TypeError("integer_validator() missing "
                            "required positional arguments")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
