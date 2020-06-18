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
        max_l, max_r = height[l], height[r]
        # 想象，只有 两个高度 max_l, max_r，向中间倒水
        water = 0
        while l < r:
            if max_l > max_r: # 右边的高度成为瓶颈，结算右边
                water += max(0, max_r - height[r])
                r -= 1 # 为什么要后减，应为第一次指向的是无效 高度
                max_r = max(max_r, height[r])
            else:
                water += max(0, max_l - height[l])
                l += 1
                max_l = max(max_l, height[l])
        return water
