from unittest import TestCase

from week15.maximum_subarray import Solution


class TestSolution(TestCase):
    def test_max_sub_array(self):
        s = Solution()
        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-1, s.maxSubArray([-1]))
