from unittest import TestCase

from week8.next_permutation import Solution


class TestSolution(TestCase):
    def test_next_permutation(self):
        s = Solution()
        nums1 = [1, 2, 3]
        s.nextPermutation(nums1)
        self.assertEqual([1, 3, 2], nums1)

        nums2 = [1, 2]
        s.nextPermutation(nums2)
        self.assertEqual([2, 1], nums2)

        nums3 = [1, 3, 2]
        s.nextPermutation(nums3)
        self.assertEqual([2, 1, 3], nums3)
