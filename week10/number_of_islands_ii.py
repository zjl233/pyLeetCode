from typing import List

from utils.misc import UnionFind


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        res: List[int] = []
        for r, c in positions:
            uf.add_node((r, c))
            for y, x in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= y < m and 0 <= x < n:
                    uf.union((r, c), (y, x))
            res.append(uf.set_num())

        return res
