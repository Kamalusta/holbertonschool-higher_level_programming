#!/usr/bin/python3
''' test cases'''
from models import base
import unittest


class test_base(unittest.TestCase):
    '''doc '''

    def test_base_id(self):
        b1 = base.Base(1)
        self.assertEqual(b1.id, 1)

    def test_baseid_node(self):
        b1 = base.Base()
        self.assertEqual(b1.id, 1)


if __name__ == '__main__':
    unittest.main()
