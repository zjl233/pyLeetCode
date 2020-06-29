from typing import List


# 暴力解
# 试着把每个数都移除一次，看移除后，数组的最长连续递增序列
# 注意，连续！！！

def longest_sqeu(nums: List[int]) -> int:
    # 洗数据
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    cur, max_ = 1, 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            cur += 1
            max_ = max(max_, cur)
        else:
            cur = 1

    return max_


def longest_sqeu_after_delete_num(nums: List[int]) -> int:
    # 洗数据
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    # 蠢办法，数组上的每个数都尝试删除一次，看看能不能产生更长的递增序列
    max_ = 0
    for i in range(len(nums)):
        max_ = max(max_, longest_sqeu(nums[:i] + nums[i + 1:]))

        # 注意加1
    return max_ + 1


def oj_main():
    # 数字输入 start ===========================
    n = int(input())  # 一共有 n 个输入，或 n 行输入

    ints = [int(s) for s in input().split()]  # 单行输入，用不到 n
    res = longest_sqeu_after_delete_num(ints)
    print(res)


if __name__ == '__main__':
    oj_main()
