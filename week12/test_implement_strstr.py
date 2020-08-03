from unittest import TestCase

from week12.implement_strstr import Solution


class TestSolution(TestCase):
    def test_str_str(self):
        s = Solution()
        self.assertEqual(2, s.strStr("hello", "ll"))
        self.assertEqual(-1, s.strStr("aaaaaa", "bba"))
