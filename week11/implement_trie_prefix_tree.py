from typing import List, Optional


class TrieNode:

    def __init__(self) -> None:
        self.pass_ = 0
        self.end = 0
        self.nexts: List[Optional[TrieNode]] = [None] * 26


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        cur.pass_ += 1
        for c in word:
            i = ord(c) - ord('a')
            if not cur.nexts[i]:
                cur.nexts[i] = TrieNode()
            cur = cur.nexts[i]
            cur.pass_ += 1

        cur.end += 1

    def delete(self, word: str) -> None:
        if self.search(word) == 0:
            return

        cur = self.root
        cur.pass_ -= 1
        for c in word:
            i = ord(c) - ord('a')
            if cur.nexts[i].pass_ == 1:
                cur.nexts[i] = None
                return
            cur = cur.nexts[i]
            cur.pass_ -= 1

        cur.end -= 1

    def search(self, word: str) -> int:
        # 查询 word 在字典树中插入了几次
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.nexts[i]:
                return 0
            cur = cur.nexts[i]

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        # 是否有单词以 prefix 开头
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.nexts[i]:
                return False
            cur = cur.nexts[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
