#!/usr/bin/python3
"""Unittest for max_integer([..])
Test cases for the max_integer function from the 6-max_integer module.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function.
    The tests include edge cases such as empty lists, lists with all equal elements, and lists with one element.
    """

    def test_ordered_list(self):
        """Test a list that is already ordered."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list that is not ordered."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test a list that contains only one element."""
        self.assertEqual(max_integer([77]), 77)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list that contains negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_equal_elements(self):
        """Test a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_none_input(self):
        """Test passing None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_input(self):
        """Test passing a string instead of a list."""
        with self.assertRaises(TypeError):
            max_integer("string")

    def test_list_of_strings(self):
        """Test a list of strings instead of integers."""
        with self.assertRaises(TypeError):
            max_integer(["hello", "world"])

if __name__ == '__main__':
    unittest.main()
