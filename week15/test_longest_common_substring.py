from unittest import TestCase

from week15.longest_common_substring import longest_common_substring


class TestSolution(TestCase):
    def test_longest_common_substring(self):
        self.assertEqual(2, longest_common_substring("bab", "caba"))
