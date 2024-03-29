#!/usr/bin/python3
'''
this will create a rectangle an give it width, height x and y value
'''
from models.base import Base


class Rectangle(Base):
    '''this will create a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''area function returns area of rectangkle'''
        return self.width * self.height

    def display(self):
        '''display function prints rectangle with # sign'''
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        '''str return a sentence'''
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        ''' gets arguments for updating'''
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        ''' returns dictionary of values'''
        dic = {"id": self.id, "width": self.width,
               "height": self.height, "x": self.x, "y": self.y}
        return dic
