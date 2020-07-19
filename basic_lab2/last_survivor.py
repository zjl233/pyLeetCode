def last(n: int) -> int:
    # 洗数据（不洗了）

    nums = [i for i in range(n + 1)]
    while len(nums) > 1:
        nums = [n for i, n in enumerate(nums) if i % 2 != 0]

    return nums[0]


def oj_main():
    # 数字输入 start ===========================
    n = int(input())  # 一共有 n 个输入，或 n 行输入
    res = last(n)
    print(res)


if __name__ == '__main__':
    # 多用例输入
    # 单用例也可以用
    while True:
        try:
            oj_main()
        except EOFError:
            break
