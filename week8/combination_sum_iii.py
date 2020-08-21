from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        path: List[int] = []
        res: List[List[int]] = []
        candidates.sort()
        self.process(candidates, 0, n, path, res, k)
        return res

    def process(self, candidates: List[int], begin: int, remain: int, path: List[int], res: List[List[int]], k: int) -> None:
        if remain < 0:
            return
        if remain == 0 and len(path) == k:
            res.append(path.copy())
            return

        for i in range(begin, len(candidates)):
            if i > begin and candidates[i] == candidates[i - 1]:
                continue

            n = candidates[i]

            path.append(n)
            self.process(candidates, i + 1, remain - n, path, res, k)
            path.pop()
