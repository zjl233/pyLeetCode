from unittest import TestCase

from week8.string_combination import Solution


class TestSolution(TestCase):
    def test_permutation(self):
        s = Solution()
        res = s.permutation("abc")
        self.assertEqual(["abc", "acb", "bac", "bca", "cab", "cba"], list(res))

        self.assertEqual(["aba", "aab", "baa"], s.permutation("aab"))
