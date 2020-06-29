from unittest import TestCase

from week7.merge_intervals import Solution


class TestSolution(TestCase):
    def test_merge(self):
        s = Solution()
        self.assertEqual([[1, 6], [8, 10], [15, 18]], s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
        self.assertEqual([[1, 5]], s.merge([[1, 4], [4, 5]]))
