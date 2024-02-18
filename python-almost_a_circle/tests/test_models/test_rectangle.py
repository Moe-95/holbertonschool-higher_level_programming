#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys
import json
import pep8

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_id(self):
        """Check if each instance of Rectangle has a unique ID."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertIsNotNone(id(r1))

    def test_init(self):
        """Verify that instances of Rectangle are created properly."""
        Base._Base__nb_objects = 0
        r2 = Rectangle(2, 10)
        self.assertIsInstance(r2, Rectangle)

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
