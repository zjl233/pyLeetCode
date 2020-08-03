import time
from random import randint
from unittest import TestCase

from basic_lab1.advanced_sorting import merge_sort, heap_sort, merge, py_merge


class Test(TestCase):
    def test_merge_sort(self):
        # 对数器比较
        # 生成 长度为 0~100 的数组，数组中的每个元素在 -100 到 +100 之间
        # 和 python 自带的 sort 比较
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(randint(0, 100))]
            nums2 = nums1.copy()
            merge_sort(nums1)
            nums2.sort()
            self.assertEqual(nums1, nums2)

    def test_heap_sort(self):
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(randint(0, 100))]
            nums2 = nums1.copy()
            heap_sort(nums1)
            nums2.sort()
            self.assertEqual(nums1, nums2)

    def test_quick_sort(self):
        for _ in range(1000):
            nums1 = [randint(-100, 100) for _ in range(randint(0, 100))]
            nums2 = nums1.copy()
            heap_sort(nums1)
            nums2.sort()
            self.assertEqual(nums1, nums2)

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
