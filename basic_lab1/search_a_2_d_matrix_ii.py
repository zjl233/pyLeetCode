from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        题目地址：
        https://www.nowcoder.com/study/live/348/1/11
        课后作业 1.11

        https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
        Python 3.6
        注：牛客网不支持 Python3，只能到 Leetocde 写了
        注：剑指 offer 04 二维数组中的查找

        题型：
        查找，带一点模拟

        解题思路：
        把二维数组旋转，右上角指向正上方，二维数组看起来就像二叉树一样
        注：很像，但有显著差异
        接着就模拟二叉树，根据 target 和 cur 的大小，选择往左还是往右

        参考：
        LeetCode 官方 solution

        难度评价：
        思维[要想一下] Coding[简单]

        time: O(n+m) // 每次都排除一行或者一列
        space: O(1)
        ac: 100%
        """
        # 洗数据
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        h, w = len(matrix), len(matrix[0])
        # 从右上角开始
        r, c = 0, w - 1
        while r < h and c >= 0:
            if target < matrix[r][c]:
                # 左
                c = c - 1
            elif target > matrix[r][c]:
                # 右
                r = r + 1
            else:
                return True

        return False
