from typing import List

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        lmt_l, lmt_r = height[l], height[r]
        water = 0
        while l < r:
            if lmt_l > lmt_r:  # 右边的高度成为瓶颈，结算右边
                r -= 1  # 这一行放在下面和和上面都一样
                water += max(0, lmt_r - height[r])
                lmt_r = max(lmt_r, height[r])
            else:
                l += 1
                water += max(0, lmt_l - height[l])
                lmt_l = max(lmt_l, height[l])
        return water
