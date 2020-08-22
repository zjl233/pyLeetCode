from unittest import TestCase

from week8.combinations import Solution


class TestSolution(TestCase):
    def test_combine(self):
        s = Solution()
        expect1 = [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [3, 4],
        ]
        res = s.combine(4, 2)
        self.assertEqual(expect1, res)
