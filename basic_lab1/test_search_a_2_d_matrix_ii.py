from unittest import TestCase

from basic_lab1.search_a_2_d_matrix_ii import Solution


class TestSolution(TestCase):
    def test_search_matrix(self):
        s = Solution()
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertTrue(s.searchMatrix(matrix, 5))
        self.assertFalse(s.searchMatrix(matrix, 20))
