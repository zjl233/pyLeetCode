from typing import List, Tuple


class Solution:
    # 题型：递归（回溯），不是 dp
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 不用洗数据了，都是有效数据

        h, w = len(board), len(board[0])
        visited = [[False for _ in range(w)] for _ in range(h)]
        # 在主函数里尝试，以 board 的任意位置作为开头，进行 dfs
        for r in range(h):
            for c in range(w):
                if word[0] == board[r][c]:
                    visited[r][c] = True
                    if self.process(board, word, 1, (r, c), visited):
                        return True
                    visited[r][c] = False
        return False

    def process(self, board: List[List[str]], word: str, i: int, loc: Tuple[int, int], visited: List[List[bool]]) -> bool:
        """
        :param board:
        :param word:
        :param i: 指向下一个，需要找的字符。如果等于单词的长度，说明单词找全了
        :param loc: 当前在 board 的哪里
        :param visited:
        :return:

        可变参数太多了，没办法 dp
        """
        # 遍历邻居，找的与下一个字符相等的，并且没有 visited 的
        # 注意，将 visited，标记为 True，可能在返回的时候，还要标记为 False
        if i == len(word):
            return True

        r, c = loc
        h, w = len(board), len(board[0])
        for y, x in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= y < h and 0 <= x < w and board[y][x] == word[i] and not visited[y][x]:
                visited[y][x] = True
                if self.process(board, word, i + 1, (y, x), visited):
                    return True
                visited[y][x] = False

        return False
