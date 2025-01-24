#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function"""

    def test_ordered_list(self):
        """Test with a list of ordered integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of unordered integers"""
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_and_floats(self):
        """Test with a list of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.8]), 4.8)

    def test_list_with_strings(self):
        """Test with a list containing strings (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])

    def test_string(self):
        """Test with a string (should return the max char)"""
        self.assertEqual(max_integer("holberton"), "t")

    def test_none(self):
        """Test with None as input (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(None)
