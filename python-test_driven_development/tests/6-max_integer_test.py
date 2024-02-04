#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to define unittests for max_integer function"""

    def test_regular_list(self):
        """Test max_integer with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats_list(self):
        """Test max_integer with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)

    def test_mixed_list(self):
        """Test max_integer with a mixed list"""
        self.assertEqual(max_integer([1, 2, 3.5, 4]), 4)
        self.assertEqual(max_integer([1, 3.3, 4, 2]), 4)

    def test_strings_list(self):
        """Test max_integer with a list of strings"""
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

if __name__ == '__main__':
    unittest.main()
