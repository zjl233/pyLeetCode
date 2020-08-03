from unittest import TestCase

from week15.palindrome_partitioning_ii import Solution, is_palindrome_dp


class TestSolution(TestCase):
    def test_min_cut(self):
        s = Solution()
        self.assertEqual(1, s.minCut("aab"))
        self.assertEqual(2, s.minCut("acdcdcdad"))
        self.assertEqual(2, s.minCut("accabc"))

    def test_is_palindrome_dp(self):
        dp = is_palindrome_dp("aabcad")
        self.assertTrue(dp[0][1])
        self.assertFalse(dp[0][2])
        self.assertFalse(dp[3][5])

    def test_min_cut_dp(self):
        s = Solution()
        self.assertEqual(1, s.minCutDP("aab"))
        self.assertEqual(2, s.minCutDP("acdcdcdad"))
        self.assertEqual(2, s.minCutDP("accaba"))


