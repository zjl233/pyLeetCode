from unittest import TestCase

from extra.new_21_game import Solution


class TestSolution(TestCase):
    def test_new21game(self):
        s = Solution()
        print(s.new21Game(4, 2, 3))
