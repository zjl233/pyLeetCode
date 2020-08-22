from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        if s in word_set:
            return True
        if not s:
            return True

        return self.process(s, 0, word_set)

    def process(self, s: str, begin: int, word_set: Set[str]) -> bool:
        if begin == len(s):
            return True

        for i in range(begin, len(s)):
            if s[begin:i + 1] in word_set:
                if self.process(s, i + 1, word_set):
                    return True

        return False

    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for begin in range(len(s) - 1, -1, - 1):
            for i in range(begin, len(s)):
                if s[begin:i + 1] in word_set and dp[i + 1]:
                    dp[begin] = True
                    break

        return dp[0]
