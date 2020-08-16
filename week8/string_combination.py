from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        chs = list(s)
        path: List[str] = []
        res: List[str] = []
        self.process(chs, path, res)
        return res

    def process(self, chs: List[str], path: List[str], res: List[str]) -> None:
        # if len(chs) == 1:
        #     path.append(chs[0])
        #     res.append(''.join(path))
        #     path.pop()
        #     return

        if len(chs) == 0:
            # path.append(chs[0])
            res.append(''.join(path))
            # path.pop()
            return

        seen = set()
        for i in range(len(chs)):
            if chs[i] in seen:
                continue
            seen.add(chs[i])

            ch = chs.pop(i)
            path.append(ch)
            self.process(chs, path, res)
            path.pop()
            chs.insert(i, ch)
