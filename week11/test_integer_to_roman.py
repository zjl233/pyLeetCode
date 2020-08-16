from unittest import TestCase

from week11.integer_to_roman import Solution


class TestSolution(TestCase):
    def test_int_to_roman(self):
        s = Solution()
        self.assertEqual("III", s.intToRoman(3))
        self.assertEqual("IV", s.intToRoman(4))
        self.assertEqual("IX", s.intToRoman(9))
        self.assertEqual("LVIII", s.intToRoman(58))
        self.assertEqual("MCMXCIV", s.intToRoman(1994))
