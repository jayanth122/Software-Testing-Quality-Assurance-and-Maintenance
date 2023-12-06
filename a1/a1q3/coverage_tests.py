import unittest

from . import token_with_escape


class CoverageTests(unittest.TestCase):
    def test_1(self):
        """Node Coverage but not Edge Coverage"""
        # Test when input contains no escape characters and a single separator
        result = token_with_escape("one|two|three")
        self.assertEqual(result, ["one", "two", "three"])

        # Test when input contains escape characters and a single separator
        result = token_with_escape("one^|two|three")
        self.assertEqual(result, ["one|two", "three"])

    def test_2(self):
        """Edge Coverage but not Edge Pair Coverage"""
        # Test when input contains escape characters and multiple separators
        result = token_with_escape("one^|two||three^^four^|||five")
        self.assertEqual(result, ["one|two", "", "three^four|", "", "five"])

    def test_3(self):
        """Edge Pair Coverage but not Prime Path Coverage"""
        # Test when input is empty
        result = token_with_escape("")
        self.assertEqual(result, [''])
