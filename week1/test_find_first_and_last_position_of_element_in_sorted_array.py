from unittest import TestCase

from week1.find_first_and_last_position_of_element_in_sorted_array import Solution


class TestSolution(TestCase):
    def test_search_range(self):
        s = Solution()
        self.assertEqual([3, 4], s.searchRange([5, 7, 7, 8, 8, 10], 8))
        self.assertEqual([-1, -1], s.searchRange([5, 7, 7, 8, 8, 10], 6))
