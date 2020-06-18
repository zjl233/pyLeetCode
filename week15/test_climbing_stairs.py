from unittest import TestCase

from week15.climbing_stairs import Solution


class TestSolution(TestCase):
    def test_climb_stairs(self):
        s = Solution()
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(3, s.climbStairs(3))
