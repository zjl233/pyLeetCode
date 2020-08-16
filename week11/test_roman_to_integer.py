from typing import List
from unittest import TestCase

from week11.roman_to_integer import Solution


class TestSolution(TestCase):
    def test_roman_to_int(self):
        s = Solution()
        self.assertEqual(3, s.romanToInt("III"))
        self.assertEqual(4, s.romanToInt("IV"))
        self.assertEqual(9, s.romanToInt("IX"))
        self.assertEqual(58, s.romanToInt("LVIII"))
        self.assertEqual(1994, s.romanToInt("MCMXCIV"))
        self.assertEqual(621, s.romanToInt("DCXXI"))

