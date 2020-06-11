from unittest import TestCase

from week12.sliding_window_maximum import Solution


class TestSolution(TestCase):
    def test_max_sliding_window(self):
        s = Solution()
        res = s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)
        print(res)

