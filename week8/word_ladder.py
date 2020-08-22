import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list = set(wordList)
        q = deque([[beginWord, 1]])

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    next_word = word[:i] + ch + word[i + 1:]
                    if next_word in word_list:
                        word_list.remove(next_word)
                        q.append([next_word, length + 1])

        return 0

