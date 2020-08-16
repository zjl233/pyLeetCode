from unittest import TestCase

from week10.number_of_islands import Solution


class TestSolution(TestCase):
    def test_num_islands(self):
        s = Solution()
        grid1 = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]

        self.assertEqual(1, s.numIslands(grid1))

        grid2 = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]

        self.assertEqual(3, s.numIslands(grid2))

