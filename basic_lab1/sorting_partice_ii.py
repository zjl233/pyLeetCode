from typing import List

from basic_lab1.advanced_sorting import merge_sort, quick_sort, heap_sort


def sorting_partice(nums: List[int], ord_flag: int):
    """
    解题思路:
    没有什么可说的，就是自己写排序

    题目地址：
    https://www.nowcoder.com/study/live/348/2/11
    课后作业 2.11
    pypy 3.6.1
    """
    # Python 自带
    # nums.sort(reverse=ord_flag == 1)

    # advanced_sorting.py 文件里有自己写的三大排序
    # 归并
    merge_sort(nums)
    # 快排
    # quick_sort(nums)
    # 堆排
    # heap_sort(nums)

    # 自己写的三个排序要用到这个判断
    if ord_flag == 1:
        nums.reverse()

def oj_main():
    # 数字输入 start ===========================
    n = int(input())  # 一共有 n 个输入，或 n 行输入
    ints = [int(s) for s in input().split()]  # 单行输入，用不到 n
    flag = int(input())

    sorting_partice(ints, flag)
    print(' '.join([str(i) for i in ints]))  # 单行输出数字数组
    # 数字输入 end  ============================


if __name__ == '__main__':
    # 多用例输入
    # 单用例也可以用
    while True:
        try:
            oj_main()
        except EOFError:
            break
