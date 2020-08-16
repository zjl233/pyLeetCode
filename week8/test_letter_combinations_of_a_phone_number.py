from unittest import TestCase

from week8.letter_combinations_of_a_phone_number import Solution


class TestSolution(TestCase):
    def test_letter_combinations(self):
        s = Solution()
        expect1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        res1 = s.letterCombinations("23")

        self.assertEqual(expect1, res1)