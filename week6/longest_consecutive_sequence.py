from typing import List

from utils.misc import UnionFind


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        d = {}
        for n in nums:
            uf.union(n, n - 1)
            uf.union(n, n + 1)
        return max(uf.size.values())
