from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path: List[int] = []
        res: List[List[int]] = []
        candidates.sort()
        self.process(candidates, 0, target, path, res)
        return res

    def process(self, candidates: List[int], begin: int, target: int, path: List[int], res: List[List[int]]) -> None:
        # if sum(path) > target:  # 剪枝
        #     return

        if sum(path) == target:
            res.append(path.copy())
            return

        for i in range(begin, len(candidates)):
            n = candidates[i]

            if sum(path) + n > target:
                break

            path.append(n)
            self.process(candidates, i, target, path, res)
            path.pop()
