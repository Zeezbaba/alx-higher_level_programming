#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaximumInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_arranged_list(self):
        """Test an arranged list of integers."""
        arranged = [1, 2, 3, 4]
        self.assertEqual(max_integer(arranged), 4)

    def test_unsorted_list(self):
        """Test an unsorted list of integers."""
        unsorted = [1, 2, 4, 3]
        self.assertEqual(max_integer(unsorted), 4)

    def test_top_max(self):
        """Test a list with a top maximum value."""
        top_max = [4, 3, 2, 1]
        self.assertEqual(max_integer(top_max), 4)

    def test_emptylist(self):
        """Test an empty list."""
        emptylist = []
        self.assertEqual(max_integer(emptylist), None)

    def test_single_list(self):
        """Test a list with a single element."""
        single_element = [7]
        self.assertEqual(max_integer(single_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_floats(self):
        """Test a list of ints and floats."""
        ints_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Zeezboss"
        self.assertEqual(max_integer(string), 'r')

    def test_strings(self):
        """Test a list of strings."""
        strings = ["Zeezboss", "is", "my", "nickname"]
        self.assertEqual(max_integer(strings), "nickname")

    def test_nul_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
