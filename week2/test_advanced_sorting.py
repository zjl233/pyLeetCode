import time
from random import randint
from unittest import TestCase

from week2.advanced_sorting import merge, merge_sort, heap_sort, py_merge


class Test(TestCase):
    def test_merge(self):
        self.assertEqual(merge([3, 6, 7, 9], [1, 3, 5, 6]), [1, 3, 3, 5, 6, 6, 7, 9])

    # compare merge and py merge
    def test_py_merge(self):
        numsl = [randint(-100, 100) for _ in range(100)]
        numsr = [randint(-100, 100) for _ in range(100)]
        numsl.sort()
        numsr.sort()
        nums1 = numsl + numsr
        nums2 = nums1.copy()

        start = time.time()
        merge(nums1, 0, 99, 199)
        mid = time.time()
        py_merge(nums2, 0, 99, 199)
        end = time.time()

        time_merge = mid - start
        time_py_merge = end - mid

        if time_merge < time_py_merge:
            print("merge faster than py_merge")
        else:
            print("merge slower than py_merge")




    def test_merge_sort(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(merge_sort([3, 1, 2, 4]), [1, 2, 3, 4])
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(100)]
            nums2 = nums1.copy()
            self.assertEqual(merge_sort(nums1), sorted(nums2))

    def test_heap_sort(self):
        nums = [3, 1, 2]
        numscp = nums.copy()
        heap_sort(nums)
        self.assertEqual(nums, sorted(numscp))
        # for _ in range(1000):
        #     nums1 = [randint(-100, 100) for _ in range(100)]
        #     nums2 = nums1.copy()
        #     heap_sort(nums1)
        #     self.assertEqual(nums1, sorted(nums2))


