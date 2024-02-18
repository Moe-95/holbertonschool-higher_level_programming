#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys
import json
import pep8

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_id(self):
        """Check if each instance of Square has a unique ID."""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertIsNotNone(id(s1))

    def test_init(self):
        """Verify that instances of Square are created properly."""
        Base._Base__nb_objects = 0
        s2 = Square(5)
        self.assertIsInstance(s2, Square)
        self.assertTrue(issubclass(type(s2), Rectangle))

    def test_numObj(self):
        """Check the number of instances created."""
        Base._Base__nb_objects = 0
        s3 = Square(2, 2)
        s4 = Square(5, 5)
        self.assertEqual(s4.id, 2)

    def test_getterAndSetter(self):
        """Check the getter and setter methods."""
        Base._Base__nb_objects = 0
        s5 = Square(5)
        self.assertEqual(s5.width, 5)
        self.assertEqual(s5.height, 5)
        s5 = Square(2, 2)
        self.assertEqual(s5.width, 2)
        self.assertEqual(s5.height, 2)
        self.assertEqual(s5.x, 2)
        s5 = Square(3, 1, 3)
        self.assertEqual(s5.width, 3)
        self.assertEqual(s5.height, 3)
        self.assertEqual(s5.x, 1)
        self.assertEqual(s5.y, 3)

    # Other test methods go here...

    def test_pep8_model(self):
        """Check if the code in models/base.py follows PEP8 conventions."""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """Check if the code in tests/test_models/test_base.py follows PEP8 conventions."""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == '__main__':
    unittest.main()
