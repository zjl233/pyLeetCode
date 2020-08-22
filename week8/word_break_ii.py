from typing import List, Set, Dict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        path: List[str] = []
        res: List[str] = []
        dp = self.canWordBreak(s, wordDict)
        word_set = set(wordDict)
        self.process(s, 0, dp, word_set, path, res)
        return res

    def process(self, s: str, begin: int, dp: List[bool], word_set: Set[str], path: List[str], res: List[str]) -> None:
        if not dp[begin]:
            return

        if begin == len(s):
            res.append(' '.join(path))
            return

        for i in range(begin, len(s)):
            if s[begin:i + 1] in word_set:
                path.append(s[begin:i + 1])
                self.process(s, i + 1, dp, word_set, path, res)
                path.pop()

    def canWordBreak(self, s: str, wordDict: List[str]) -> List[bool]:
        word_set = set(wordDict)

        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for begin in range(len(s) - 1, -1, - 1):
            for i in range(begin, len(s)):
                if s[begin:i + 1] in word_set and dp[i + 1]:
                    dp[begin] = True
                    break

        return dp
