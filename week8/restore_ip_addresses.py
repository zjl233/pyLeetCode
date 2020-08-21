from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        path: List[str] = []
        res: List[str] = []
        self.process(s, 0, path, res)
        return res

    def process(self, s: str, begin: int, path: List[str], res: List[str]) -> None:
        if len(path) == 4:
            if begin == len(s):
                res.append('.'.join(path))
            return

        if len(s) - begin < (4 - len(path)) or len(s) - begin > 3 * (4 - len(path)):
            return

        for i in range(3):
            if begin + i >= len(s):
                break

            if self.is_valid(s, begin, begin + i):
                path.append(s[begin: begin + i + 1])
                self.process(s, begin + i + 1, path, res)
                path.pop()

    def is_valid(self, s: str, left: int, right: int) -> bool:
        if right - left + 1 > 1 and s[left] == '0':
            return False

        num = int(s[left:right + 1])
        return num <= 255
