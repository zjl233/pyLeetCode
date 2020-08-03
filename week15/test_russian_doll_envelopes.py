from unittest import TestCase

from week15.russian_doll_envelopes import Solution


class TestSolution(TestCase):
    def test_max_envelopes(self):
        s = Solution()
        self.assertEqual(3, s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
