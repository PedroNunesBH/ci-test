"""
Module to test add function in main.py file
"""

import unittest

from app.main import add


class TestAddFunction(unittest.TestCase):
    """
    Class to test function add of main.py file
    """

    def test_add_positive_numbers(self):
        """
        Test positive numbers add
        """

        self.assertEqual(add(10.0, 5.0), 15.0)

    def test_negative_numbers(self):
        """
        Test negative numbers add
        """

        self.assertEqual(add(-1.0, -1.0), -2.0)
