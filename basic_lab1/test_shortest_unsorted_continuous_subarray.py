from unittest import TestCase

from basic_lab1.shortest_unsorted_continuous_subarray import Solution


class TestSolution(TestCase):
    def test_find_unsorted_subarray(self):
        s = Solution()
        self.assertEqual(5, s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
        self.assertEqual(4, s.findUnsortedSubarray([1, 5, 3, 4, 2, 6, 7]))
