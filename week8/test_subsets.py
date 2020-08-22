from unittest import TestCase

from week8.subsets import Solution


class TestSolution(TestCase):
    def test_subsets(self):
        s = Solution()
        expect1 = [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
        res = s.subsets([1, 2, 3])
        self.assertEqual(expect1, res)

        res2 = s.subsets([1,2,3,4])
        print(res2)
        self.assertEqual(16, len(res2))