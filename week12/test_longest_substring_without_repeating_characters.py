from unittest import TestCase

from week12.longest_substring_without_repeating_characters import Solution


class TestSolution(TestCase):
    def test_length_of_longest_substring(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
