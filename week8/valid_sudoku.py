from itertools import product
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for r in range(n):
            st = set()
            for c in range(n):
                ch = board[r][c]
                if ch != '.' and ch in st:
                    return False
                else:
                    st.add(ch)

        for c in range(n):
            st = set()
            for r in range(n):
                ch = board[r][c]
                if ch != '.' and ch in st:
                    return False
                else:
                    st.add(ch)

        for y, x in product([0, 3, 6], [0, 3, 6]):
            st = set()

            for r in range(y, y + 3):
                for c in range(x, x + 3):
                    ch = board[r][c]
                    if ch != '.' and ch in st:
                        return False
                    else:
                        st.add(ch)

        return True
