from unittest import TestCase

from week12.valid_parentheses import Solution


class TestSolution(TestCase):
    def test_is_valid(self):
        s = Solution()
        self.assertTrue(s.isValid('()'))
        self.assertTrue(s.isValid("()[]{}"))
        self.assertTrue(s.isValid("{[]}"))
        self.assertFalse(s.isValid("(]"))
        self.assertFalse(s.isValid("([)]"))
