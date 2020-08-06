from unittest import TestCase

from week6.course_schedule_ii import Solution


class TestSolution(TestCase):
    def test_find_order(self):
        s = Solution()
        res1 = s.findOrder(1, [])
        self.assertEqual([0], res1)

        res2 = s.findOrder(2, [[1, 0]])
        self.assertEqual([0, 1], res2)

        res3 = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        self.assertEqual([0, 1, 2, 3], res3)
