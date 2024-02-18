#!/usr/bin/python3
''' test cases'''
from models.rectangle import Rectangle
import unittest


class Test_Rectangle(unittest.TestCase):
    '''doc '''

    def test_atr(self):
        b1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)
        self.assertEqual(b1.id, 5)

    def test_area(self):
        b1 = Rectangle(10, 2)
        self.assertEqual(b1.area(), 20)

    def test_typeError(self):
        with self.assertRaises(TypeError):
             Rectangle("k", 2)
        with self.assertRaises(TypeError):
             Rectangle(2, "k")
        with self.assertRaises(TypeError):
             Rectangle(2, 3, "k")
        with self.assertRaises(TypeError):
             Rectangle(2, 3, 4, "k")

    def test_valueError(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)
        

    def test_str(self):
        b1 = Rectangle(4, 5, 1, 1, 1)
        self.assertEqual(str(b1), "[Rectangle] (1) 1/1 - 4/5")

    def test_update1(self):
        b1 = Rectangle(4, 5, 1, 1, 1)
        b1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(b1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update2(self):
        b1 = Rectangle(4, 5, 1, 1, 1)
        b1.update(x = 7)
        self.assertEqual(b1.x, 7)

    def test_dic(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}) 

    def test_create(self):
        dummy = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(dummy.id, 89)
        dummy1 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(dummy1.id, 89)
        self.assertEqual(dummy1.width, 1)
        dummy3 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(str(dummy3), '[Rectangle] (89) 3/4 - 1/2' ) 
        
if __name__ == '__main__':
    unittest.main()

        
