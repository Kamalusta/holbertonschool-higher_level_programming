#!/usr/bin/python3
''' test cases'''
from models.base import Base
import unittest


class test_base(unittest.TestCase):
    '''doc '''

    def test_base_id(self):
        self.assertEqual(Base(3).id, 3)

    def test_baseid_node(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_to_json(self):
        dictionary = {"id": 10}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 10}]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_from_json(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])


if __name__ == '__main__':
    unittest.main()
