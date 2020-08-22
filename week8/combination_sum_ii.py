from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path: List[int] = []
        res: List[List[int]] = []
        candidates.sort()
        self.process(candidates, 0, target, path, res)
        return res

    def process(self, candidates: List[int], begin: int, remain: int, path: List[int], res: List[List[int]]) -> None:
        if remain < 0:
            return
        if remain == 0:
            res.append(path.copy())
            return

        for i in range(begin, len(candidates)):
            if i > begin and candidates[i] == candidates[i - 1]:
                continue

            n = candidates[i]

            path.append(n)
            self.process(candidates, i + 1, remain - n, path, res)
            path.pop()

