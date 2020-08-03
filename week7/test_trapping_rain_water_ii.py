from unittest import TestCase

from week7.trapping_rain_water_ii import Solution


class TestSolution(TestCase):
    def test_trap_rain_water(self):
        s = Solution()
        matrix = [
            [1, 4, 3, 1, 3, 2],
            [3, 2, 1, 3, 2, 4],
            [2, 3, 3, 2, 3, 1]
        ]
        self.assertEqual(4, s.trapRainWater(matrix))
