from unittest import TestCase

from week2.sort_colors import Solution


class TestSolution(TestCase):
    def test_sort_colors(self):
        sort_colors = Solution().sortColors
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])
