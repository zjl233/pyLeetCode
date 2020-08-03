from unittest import TestCase

from week7.ipo import Solution


class TestSolution(TestCase):
    def test_find_maximized_capital(self):
        s = Solution()
        self.assertEqual(4, s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
        self.assertEqual(6, s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
        self.assertEqual(23, s.findMaximizedCapital(3, 2, [5, 1, 7, 9, 400], [3, 7, 1, 6, 100]))
