# -*- coding:utf-8 -*-
class Solution:
    # 数组中的逆序对
    # https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5
    def InversePairs(self, data):
        # write code here
        return self.process(data, 0, len(data) - 1)

    def process(self, data, l, r):
        # base case
        if l == r:
            return 0

        m = (l + r) // 2

        return self.process(data, l, m) + self.process(data, m + 1, r) + self.merge(data, l, m, r)

    def merge(self, data, l, m, r):
        help = [0] * (r - l + 1)
        i = 0
        p1, p2 = l, m + 1
        res = 0

        while p1 <= m and p2 <= r:
            if data[p1] <= data[p2]:
                help[i] = data[p1]
                i += 1
                p1 += 1
            else:
                res += m - p1 + 1
                help[i] = data[p2]
                i += 1
                p2 += 1

        while p1 <= m:
            help[i] = data[p1]
            i += 1
            p1 += 1
        while p2 <= r:
            help[i] = data[p2]
            i += 1
            p2 += 1

        for i in range(len(help)):
            data[l + i] = help[i]

        return res
