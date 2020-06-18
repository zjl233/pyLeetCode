from unittest import TestCase

from week7.trapping_rain_water import Solution


class TestSolution(TestCase):
    def test_trap(self):
        s = Solution()
        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
