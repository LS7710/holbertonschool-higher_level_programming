#!/usr/bin/python3
"""Unittest for max_integer([..])
This script tests the max_integer function to ensure it correctly finds the maximum integer in a list, or returns None for an empty list.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines the test cases for the max_integer function."""

    def test_positive_integers(self):
        """Test a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([77]), 77)

    def test_duplicates(self):
        """Test a list with duplicate maximum values."""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_non_integer(self):
        """Test a list with non-integer types (optional, raises TypeError)."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three'])

if __name__ == '__main__':
    unittest.main()
