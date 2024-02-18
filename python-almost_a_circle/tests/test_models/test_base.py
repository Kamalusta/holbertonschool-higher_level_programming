#!/usr/bin/python3
''' test cases'''
from models.base import Base
import unittest


class test_base(unittest.TestCase):
    '''doc '''

    def test_base_id(self):
        b1 = Base(3)
        self.assertEqual(b1.id, 3)

    def test_baseid_node(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == '__main__':
    unittest.main()
