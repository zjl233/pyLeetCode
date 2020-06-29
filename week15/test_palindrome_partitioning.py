from unittest import TestCase

from week15.palindrome_partitioning import Solution


class TestSolution(TestCase):
    def test_partition(self):
        s = Solution()
        res = [
            ["a", "a", "b"],
            ["aa", "b"],
        ]

        self.assertEqual(res, s.partition("aab"))
        self.assertEqual([["b", "b"], ["bb"]], s.partition("bb"))
