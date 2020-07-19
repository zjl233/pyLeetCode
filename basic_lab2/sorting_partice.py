from typing import List, Tuple


def sorting_partice(pairs: List[Tuple[str, int]], ord_flag: int):
    """
    题目地址：
    课后作业 3.7
    pypy 3.6.1

    偷个懒~~
    """
    pairs.sort(key=lambda pair: pair[1], reverse=ord_flag == 0)


def oj_main():
    # 数字输入 start ===========================
    n = int(input())  # 一共有 n 个输入，或 n 行输入
    flag = int(input())

    pairs: List[Tuple[str, int]] = []
    for _ in range(n):
        line = input()
        name, score = line.split()[0], int(line.split()[1])
        pairs.append((name, score))

    sorting_partice(pairs, flag)
    for pair in pairs:
        print(pair[0], pair[1])


if __name__ == '__main__':
    # 多用例输入
    # 单用例也可以用
    while True:
        try:
            oj_main()
        except EOFError:
            break

