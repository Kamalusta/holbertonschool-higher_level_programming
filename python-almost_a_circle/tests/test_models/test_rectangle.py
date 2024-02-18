#!/usr/bin/python3
''' test cases'''
from models.rectangle import Rectangle
import unittest
import os


class Test_Rectangle(unittest.TestCase):
    '''doc '''

    def test_atr(self):
        b1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)
        self.assertEqual(b1.id, 5)
        self.assertEqual(str(b1), '[Rectangle] (5) 3/4 - 10/2')

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

    def test_save_to_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file(None)
        with open("Rectangle.json", encoding="UTF-8") as fread:
            self.assertEqual(fread.read(), '[]')
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", encoding="UTF-8") as fread:
            self.assertEqual(fread.read(), '[]')
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([Rectangle(1, 2, id = 5)])
        with open("Rectangle.json", encoding="UTF-8") as fread:
            self.assertEqual(fread.read(), '[{"id": 5, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        res = Rectangle.load_from_file()
        self.assertEqual(res, [])
            
    def test_load_from_file2(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        r1 = Rectangle(5, 5)

        input = [r1]
        Rectangle.save_to_file(input)
        output = Rectangle.load_from_file()

        self.assertEqual(input[0].__str__(), output[0].__str__())
        
        

        
if __name__ == '__main__':
    unittest.main()

        
