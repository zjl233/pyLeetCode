from typing import List


# 三重暴力循环，哈哈

def is_triangle(a: int, b: int, c: int) -> bool:
    # 两边之和大于第三边，两边之差小于第三边
    return a + b > c and a + c > b and b + c > a \
           and \
           abs(a - b) < c and abs(a - c) < b and abs(b - c) < a


def assembly_ways(edges: List[int]) -> int:
    n = len(edges)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_triangle(edges[i], edges[j], edges[k]):
                    cnt += 1

    return cnt


def oj_main():
    # 数字输入 start ===========================
    n = int(input())  # 一共有 n 个输入，或 n 行输入

    ints = [int(s) for s in input().split()]  # 单行输入，用不到 n

    res = assembly_ways(ints)
    print(res)


if __name__ == '__main__':
    oj_main()
