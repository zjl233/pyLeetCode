import string
from collections import defaultdict
from typing import List, DefaultDict


# 这是广度优先遍历
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        layer = {beginWord: [[beginWord]]}
        while layer:
            newLayer: DefaultDict[str, List[List[str]]] = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                else:
                    for i in range(len(word)):
                        for ch in string.ascii_lowercase:
                            next_word = word[:i] + ch + word[i + 1:]
                            if next_word in wordSet:
                                newLayer[next_word] += [path + [next_word] for path in layer[word]]
            wordSet -= set(newLayer.keys())
            layer = newLayer
        return []
