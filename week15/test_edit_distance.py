from unittest import TestCase

from week15.edit_distance import Solution


class TestSolution(TestCase):
    def test_min_distance(self):
        s = Solution()
        self.assertEqual(3, s.minDistance("horse", "ros"))
        self.assertEqual(5, s.minDistance("intention", "execution"))
