from typing import List


def merge_sort(nums: List[int]):
    if len(nums) < 2:
        return nums

    process(nums, 0, len(nums) - 1)

    return nums


def process(nums: List[int], l: int, r: int):
    # base case
    if l == r:
        return

    m = (l + r) // 2
    process(nums, l, m)
    process(nums, m + 1, r)

    merge(nums, l, m, r)


def merge(nums: List[int], l: int, m: int, r: int):
    help = [0] * (r - l + 1)
    i = 0
    p1, p2 = l, m + 1

    while p1 <= m and p2 <= r:
        if nums[p1] <= nums[p2]:  # 注意，相等时先放入右边，考虑 [2 王， 2 张] 的情况
            help[i] = nums[p1]
            p1 += 1
            i += 1
        else:
            help[i] = nums[p2]
            p2 += 1
            i += 1

    while p1 <= m:
        help[i] = nums[p1]
        p1 += 1
        i += 1
    while p2 <= r:
        help[i] = nums[p2]
        p2 += 1
        i += 1

    nums[l: r + 1] = help  # 注意 r + 1；比 循环更快
    # for i, _ in enumerate(help):
    #     nums[l + i] = help[i]


def py_merge(data: List[int], l: int, m: int, r: int) -> int:
    help = []  # 使用 append，没有使用 i
    p1, p2 = l, m + 1
    res = 0

    while p1 <= m and p2 <= r:
        if data[p1] <= data[p2]:
            res += (r - p2 + 1) * data[p1]

            help.append(data[p1])
            p1 += 1
        else:
            help.append(data[p2])
            p2 += 1

    while p1 <= m:
        help.append(data[p1])
        p1 += 1
    while p2 <= r:
        help.append(data[p2])
        p2 += 1

    data[l: r + 1] = help  # 注意 r + 1

    return res



# 还有点问题
def heap_sort(nums: List[int]):
    if len(nums) < 2:
        return

    # 自底向上 heapify
    for i in range(len(nums) - 1, -1, -1):
        heapify(nums, i, len(nums))
    heap_size = len(nums)

    # 交换第一个数，和最后一个数，heap_size--，heapify(0)
    nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
    heap_size -= 1

    while heap_size > 0:
        heapify(nums, 0, heap_size)
        heap_size -= 1
        nums[0], nums[heap_size] = nums[heap_size], nums[0]


# 看某个数是否可以下沉，一直到下边界 heap_size
def heapify(nums: List[int], idx: int, heap_size: int):
    left = idx * 2 + 1
    while left < heap_size:
        right = left + 1
        largest = right if right < heap_size and nums[right] > nums[left] else left
        largest = largest if nums[largest] > nums[idx] else idx
        if largest == idx:
            break
        idx = largest
        left = idx * 2 + 1


# 看某个数是否可以上浮，一直到上边界 0
def heap_insert(nums: List[int], idx: int):
    parent = (idx - 1) // 2
    while idx > 0 and nums[idx] > nums[parent]:
        nums[idx], nums[parent] = nums[parent], nums[idx]
        idx = parent


def quick_sort(nums: List[int]):
    return nums
