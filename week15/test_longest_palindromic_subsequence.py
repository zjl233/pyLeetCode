from unittest import TestCase

from week15.longest_palindromic_subsequence import Solution, longest_palindrome_subsequence_brute_recursive


class TestSolution(TestCase):
    def test_longest_palindrome_subseq(self):
        s = Solution()
        self.assertEqual(4, s.longestPalindromeSubseq("bbbab"))
        self.assertEqual(2, s.longestPalindromeSubseq("cbbd"))

    def test_longest_palindrome_subsequence_brute_recursive(self):
        self.assertEqual(4, longest_palindrome_subsequence_brute_recursive("bbbab"))
