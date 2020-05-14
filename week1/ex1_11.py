# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 边际情况
        if len(array) == 0 or len(array[0]) == 0:
            return False

        h, w = len(array), len(array[0])
        # 从右上角起
        r, c = 0, w - 1
        while r <= h - 1 and c >= 0:
            if target == array[r][c]:
                return True
            elif target < array[r][c]:
                c -= 1
            else:
                r += 1
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    print(s.Find(9, matrix))
    print(s.Find(22, matrix))
