from unittest import TestCase

from week6.course_schedule import Solution


class TestSolution(TestCase):
    def test_can_finish(self):
        s = Solution()
        self.assertTrue(s.canFinish(2, [[1, 0]]))


