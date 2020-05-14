from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    # 每次两两比较相邻的数
    # 将大的放到右边

    # 每次排列区间的右端 -1

    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    # 每次找到最小数的 minIdx，与第一个数交换

    # 每次排列区间的左端 +1

    for i in range(len(nums)):
        min_idx = i
        for j in range(i, len(nums)):
            min_idx = j if nums[j] < nums[min_idx] else min_idx
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def insertion_sort(nums: List[int]) -> List[int]:
    # 每次向前看，如果比前面🙈的数小，就交换
    # 大于等于前面的数，停止

    # 每次排好的有序区间长度 +1

    for i in range(1, len(nums)):
        for j in range(i, 0, -1):  # [i..1]
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break
    return nums
