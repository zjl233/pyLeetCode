from typing import List


# 这一题好像很简单啊，是我想错了吗？
# i = 1 ~ len(nums)
# 依次转置 nums[:i]
def reverse_sequence(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[:i + 1] = reversed(nums[:i + 1])

    return nums


def oj_main():
    # 数字输入 start ===========================
    n = int(input())  # 一共有 n 个输入，或 n 行输入

    ints = [int(s) for s in input().split()]  # 单行输入，用不到 n

    ints_res: List[int] = reverse_sequence(ints)
    print(' '.join([str(i) for i in ints_res]))  # 单行输出数字数组


if __name__ == '__main__':
    oj_main()
