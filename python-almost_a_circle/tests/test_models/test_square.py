#!/usr/bin/python3
'''test cases'''
from models.square import Square
import unittest


class Test_Square(unittest.TestCase):
    '''doc'''
    def test_arg(self):
        sqr = Square(1, 2, 3, 4)
        self.assertEqual(str(sqr),"[Square] (4) 2/3 - 1")
        
    def test_typeError(self):
        with self.assertRaises(TypeError):
             Square("k")
        with self.assertRaises(TypeError):
             Square(2, "k")
        with self.assertRaises(TypeError):
             Square(2, 3, "k")

    def test_valueError(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_str(self):
        s1 = Square(4, 5, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 5/1 - 4")
    
    def test_dic(self):
        s1 = Square(10, 1, 9, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 10,'x': 1, 'y': 9})

    def test_update1(self):
        s1 = Square(4, 1, 1, 1)
        s1.update(89, 2, 3, 5)
        self.assertEqual(str(s1), "[Square] (89) 3/5 - 2")

    def test_update2(self):
        s1 = Square(4, 5, 1, 1)
        s1.update(x = 7)
        self.assertEqual(s1.x, 7)

    def test_create(self):
        dummy = Square.create(**{ 'id': 89 })
        self.assertEqual(dummy.id, 89)
        dummy1 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(dummy1.id, 89)
        self.assertEqual(dummy1.size, 1)
        dummy3 = Square.create(**{ 'id': 89, 'size': 1, 'x': 3, 'y': 4 })
        self.assertEqual(str(dummy3), '[Square] (89) 3/4 - 1')
