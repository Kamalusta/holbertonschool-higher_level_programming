#!/usr/bin/python3
'''
Square class which makes square with values
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            arg = ["id", "size", "x", "y"]
            for i, v in enumerate(args):
                if i < len(arg):
                    setattr(self, arg[i], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
