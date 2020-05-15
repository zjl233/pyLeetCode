from typing import List


def little_sum(data: List[int]) -> int:
    return process(data, 0, len(data) - 1)


def process(data: List[int], l: int, r: int) -> int:
    # base case
    if l == r:
        return 0

    m = (l + r) // 2

    return process(data, l, m) + process(data, m + 1, r) + merge(data, l, m, r)


def merge(data: List[int], l: int, m: int, r: int) -> int:
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



if __name__ == '__main__':

    import sys

    for line in sys.stdin:
        _ = int(line)  # 没用
        strs = sys.stdin.readline().split()
        nums = [int(str) for str in strs]
        print(little_sum(nums))
