from unittest import TestCase

from week8.word_ladder_ii import Solution


class TestSolution(TestCase):
    def test_find_ladders(self):
        s = Solution()
        expect1 = [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"],

        ]
        res = s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        self.assertEqual(expect1, res)
