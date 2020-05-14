from random import randint
from unittest import TestCase

from week1.basic_sorting import bubble_sort, selection_sort, insertion_sort


class Test(TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([]), [])
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(100)]
            nums2 = nums1.copy()
            self.assertEqual(bubble_sort(nums1), sorted(nums2))

    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(selection_sort([]), [])
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(100)]
            nums2 = nums1.copy()
            self.assertEqual(selection_sort(nums1), sorted(nums2))

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(insertion_sort([]), [])
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(100)]
            nums2 = nums1.copy()
            self.assertEqual(insertion_sort(nums1), sorted(nums2))
