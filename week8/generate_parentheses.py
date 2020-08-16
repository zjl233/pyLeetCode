from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        res: List[str] = []
        path: List[str] = []

        self.process(0, 0, n, path, res)
        return res

    def process(self, left: int, right: int, n: int, path: List[str], res: List[str]):
        """
        :param left: 当前 path 中，左括号的数量
        :param right: 当前 path 中，右括号的数量
        :param n:
        :param path:
        :param res:
        :return:
        """

        if right > left:
            """
            )
            ())
            剪枝
            """
            return

        if left == right == n:
            res.append(''.join(path))
            return

        if left < n:
            path.append('(')
            self.process(left + 1, right, n, path, res)
            path.pop()
        if right < n:
            path.append(')')
            self.process(left, right + 1, n, path, res)
            path.pop()
