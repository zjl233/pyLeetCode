from unittest import TestCase

from week7.interleaving_string import Solution


class TestSolution(TestCase):
    def test_is_interleave(self):
        s = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        self.assertEqual(True, s.isInterleave(s1, s2, s3))
        s3 = "aadbbbaccc"
        self.assertEqual(False, s.isInterleave(s1, s2, s3))
