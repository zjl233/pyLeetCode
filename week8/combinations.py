from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cands = list(range(1, n + 1))
        path: List[int] = []
        res: List[List[int]] = []

        self.process(cands, 0, path, k, res)

        return res

    def process(self, cands: List[int], begin: int, path: List[int], k: int, res: List[List[int]]) -> None:
        if len(path) == k:
            res.append(path.copy())
            return

        for i in range(begin, len(cands)):
            n = cands[i]

            path.append(n)
            self.process(cands, i + 1, path, k, res)
            path.pop()

