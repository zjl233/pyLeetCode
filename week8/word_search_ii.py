from collections import defaultdict
from typing import List, Tuple


class TrieNode:

    def __init__(self) -> None:
        self.end = ""  # 以该节点结尾的单词
        self.nexts = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.nexts[c]
        cur.end = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 洗数据
        if not board or not board[0]:
            return []
        if not words:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)
        node = trie.root

        res: List[str] = []
        h, w = len(board), len(board[0])
        for r in range(h):
            for c in range(w):
                if board[r][c] in node.nexts:
                    bak = board[r][c]
                    board[r][c] = '#'

                    self.process(board, words, (r, c), node.nexts[bak], res)

                    board[r][c] = bak

        return res

    def process(self, board: List[List[str]], words: List[str], loc: Tuple[int, int], node: TrieNode, res: List[str]):
        if node.end:
            res.append(node.end)
            node.end = None

        r, c = loc
        h, w = len(board), len(board[0])
        for y, x in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= y < h and 0 <= x < w and board[y][x] != "#" and board[y][x] in node.nexts:
                bak = board[y][x]
                board[y][x] = '#'

                self.process(board, words, (y, x), node.nexts[bak], res)

                board[y][x] = bak
