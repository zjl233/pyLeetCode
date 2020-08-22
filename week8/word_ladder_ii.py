from typing import List, Set


class Solution:
    def __init__(self):
        self.min_len = float('inf')

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        words = set(wordList)
        path: List[str] = [beginWord]
        res: List[List[str]] = []
        self.process(beginWord, endWord, words, path, res)
        if len(res) == 0:
            return res

        min_len = len(min(res, key=len))
        return [p for p in res if len(p) == min_len]

    def process(self, beginWord: str, endWord: str, words: Set[str], path: List[str], res: List[List[str]]) -> None:
        if len(path) > self.min_len:
            return

        if len(path) >= 1 and path[-1] == endWord:
            res.append(path.copy())
            self.min_len = min(self.min_len, len(path))
            return

        for word in self.diff_1s(beginWord, words):
            path.append(word)
            self.process(word, endWord, words - {word}, path, res)
            path.pop()

    def diff_1s(self, beginWord: str, words: Set[str]) -> List[str]:
        res: List[str] = []
        for word in words:
            if sum([1 if a != b else 0 for a, b in zip(word, beginWord)]) == 1:
                res.append(word)
        return res
