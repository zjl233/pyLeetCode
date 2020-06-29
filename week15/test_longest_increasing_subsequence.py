from unittest import TestCase

from week15.longest_increasing_subsequence import Solution


class TestSolution(TestCase):
    def test_length_of_lis(self):
        s = Solution()
        self.assertEqual(4, s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(1, s.lengthOfLIS([7, 7, 7]))
        self.assertEqual(5, s.lengthOfLIS([2, 1, 5, 3, 6, 4, 8, 9, 7]))
        self.assertEqual(5, s.lengthOfLIS([2, 1, 5, 3, 6, 4, 8, 9, 7]))
        self.assertEqual(3, s.lengthOfLIS([1, 2, 8, 6, 4]))
