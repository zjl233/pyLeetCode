from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [
                ["Q"]
            ]

        grid = []
        solutions: List[List[int]] = []
        self.process(0, grid, n, solutions)
        return self.puzzle_from_solutions(solutions, n)

    def process(self, r: int, grid: List[int], size: int, solutions: List[List[int]]) -> None:
        if r == size:
            solutions.append(grid.copy())
            return

        for c in range(size):
            if self.is_safe(r, c, grid):
                grid.append(c)
                self.process(r + 1, grid, size, solutions)
                grid.pop()

    def is_safe(self, r: int, c: int, grid: List[int]):
        for y, x in enumerate(grid):
            # if y == r:
            #     return False
            if x == c:
                return False
            if abs((y - r) / (x - c)) == 1:
                return False

        return True

    def puzzle_from_solutions(self, solutions: List[List[int]], size: int) -> List[List[str]]:
        reses: List[List[str]] = []
        for solution in solutions:
            res: List[str] = []
            for n in solution:
                chs = ["." if i != n else "Q" for i in range(size)]
                res.append(''.join(chs))

            reses.append(res)
        return reses

