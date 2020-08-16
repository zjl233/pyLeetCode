from unittest import TestCase

from week8.generate_parentheses import Solution


class TestSolution(TestCase):
    def test_generate_parenthesis(self):
        s = Solution()
        expect1 = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
        res = s.generateParenthesis(3)
        self.assertEqual(expect1, res)


        expect2 = [
            "()"
        ]
        res = s.generateParenthesis(1)
        self.assertEqual(expect2, res)
