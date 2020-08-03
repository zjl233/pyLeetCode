from unittest import TestCase

from basic_lab2.insert_interval import Solution


class TestSolution(TestCase):

    def test_insert(self):
        s = Solution()
        self.assertEqual([[1, 5], [6, 9]], s.insert([[1, 3], [6, 9]], [2, 5]))
        self.assertEqual([[1, 2], [3, 10], [12, 16]], s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
