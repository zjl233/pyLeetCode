import random
from typing import List, Tuple


def merge_sort(nums: List[int]) -> None:
    if len(nums) < 2:
        return

    process(nums, 0, len(nums) - 1)


def process(nums: List[int], l: int, r: int) -> None:
    # base case
    if l == r:
        return

    m = (l + r) // 2
    process(nums, l, m)
    process(nums, m + 1, r)

    merge(nums, l, m, r)


def merge(nums: List[int], l: int, m: int, r: int) -> None:
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

    # 修改原始数组
    nums[l: r + 1] = help  # 注意 r + 1；比 循环更快
    # for i, _ in enumerate(help):
    #     nums[l + i] = help[i]


def py_merge(data: List[int], l: int, m: int, r: int) -> None:
    help = []  # 使用 append，没有使用 i
    p1, p2 = l, m + 1

    while p1 <= m and p2 <= r:
        if data[p1] <= data[p2]:
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


# left: 2*i + 1
# right: 2*i + 2
# parent: (i-1) // 2
# 最后一个节点: heap_size-1
# 最后一个有孩子的节点: (heap_size-2) // 2
# 大根堆，因为要让结果为升序
def heap_sort(nums: List[int]) -> None:
    if len(nums) < 2:
        return

    heap_size = len(nums)

    # 自底向上 heapify
    # 只有，有孩子的节点需要 heapify
    for i in range((heap_size - 2) // 2, -1, -1):
        heapify(nums, i, len(nums))

    # 交换第一个数，和最后一个数，heap_size--，heapify(0)
    while heap_size >= 1:
        nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
        heap_size -= 1
        heapify(nums, 0, heap_size)


# 看某个数是否可以下沉，一直到下边界 heap_size
# 大根堆，因为要让结果为升序
def heapify(nums: List[int], idx: int, heap_size: int) -> None:
    while idx <= (heap_size - 2) // 2:
        left = idx * 2 + 1
        right = idx * 2 + 2
        largest = idx

        # 注意，可能没有右节点
        for cur in [left, right]:
            if cur < heap_size and nums[largest] < nums[cur]:
                largest = cur

        if largest == idx:
            break
        else:
            nums[idx], nums[largest] = nums[largest], nums[idx]
            idx = largest


# 看某个数是否可以上浮，一直到上边界 0
def heap_insert(nums: List[int], idx: int) -> None:
    parent = (idx - 1) // 2
    while idx > 0 and nums[idx] > nums[parent]:
        nums[idx], nums[parent] = nums[parent], nums[idx]
        idx = parent


def quick_sort(nums: List[int]) -> None:
    if len(nums) < 2:
        return
    qprocess(nums, 0, len(nums) - 1)


# 递归调用函数
def qprocess(nums: List[int], l: int, r: int) -> None:
    if l >= r:
        return
    itv = three_way_partition(nums, l, r)  # 等于 nums[pivot] 的区间，左闭，右闭
    # itv 区间已经排好了，还要处理没排好的区间
    qprocess(nums, l, itv[0] - 1)
    qprocess(nums, itv[1] + 1, r)


# 三路快拍
# 返回 =区，左闭，右闭
def three_way_partition(nums: List[int], l: int, r: int) -> Tuple[int, int]:
    pivot = random.randint(l, r)  # 选择 pivot
    nums[pivot], nums[r] = nums[r], nums[pivot]
    # lt 在待排函数的外侧，gt 在 pivot 位置，所以也相当于在外侧
    # [l:lt] 是 < 区
    # [gt:r] 是 > 区
    # (lt,i) 是 = 区
    lt, gt = l - 1, r
    # i 指向右边界右边一格
    i = l
    while i < gt:
        if nums[i] < nums[r]:
            # 想象一下推书的场景
            lt += 1
            nums[i], nums[lt] = nums[lt], nums[i]
            i += 1
        elif nums[i] > nums[r]:
            # i 不动
            gt -= 1
            nums[i], nums[gt] = nums[gt], nums[i]
        else:
            # 扩大等于区间
            i += 1
    # 在 swap 之前 i 🈴和 gt 指向  =区的右边界右边一格
    nums[gt], nums[r] = nums[r], nums[gt]
    # 最终 lt =区 的右边一格
    # gt 和 i，指向 =区 右边界之上
    return lt + 1, gt  # 为什么传 等于区间，而不是左边界和有边界，为了和二路快排一致，二路快排传递的是等于 pivot 的指针
