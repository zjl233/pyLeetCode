from typing import List, Tuple


def painting_steps(board: List[List[str]]) -> int:
    """
    题目地址：
    https://www.nowcoder.com/study/live/350/2/7
    pypy 3.6.1

    解题思路：
    将色彩还原
    B -> X
    Y -> X

    G 先还原成 (B 或 Y)，再还原成 X

    time: O(n) // 最多将每个格子涂 2 次
    space: O(1)
    ac: 100%
    """

    # 不用洗数据

    h, w = len(board), len(board[0])
    cnt = 0
    for r in range(h):
        for c in range(w):
            if board[r][c] == 'Y':
                cnt += 1
                remove_yellow(board, (r, c))
            elif board[r][c] == 'B':
                cnt += 1
                remove_blue(board, (r, c))
            elif board[r][c] == 'G':
                cnt += 2
                board[r][c] = 'X'
                remove_yellow(board, (r + 1, c + 1))
                remove_blue(board, (r + 1, c - 1))

    return cnt


def remove_yellow(board: List[List[str]], loc: Tuple[int, int]):
    r, c = loc
    h, w = len(board), len(board[0])
    while 0 <= r < h and 0 <= c < w:
        if board[r][c] == 'Y':
            board[r][c] = 'X'
        elif board[r][c] == 'G':
            board[r][c] = 'B'
        else:
            break
        r, c = r + 1, c + 1


def remove_blue(board: List[List[str]], loc: Tuple[int, int]):
    r, c = loc
    h, w = len(board), len(board[0])
    while 0 <= r < h and 0 <= c < w:
        if board[r][c] == 'B':
            board[r][c] = 'X'
        elif board[r][c] == 'G':
            board[r][c] = 'Y'
        else:
            break
        r, c = r + 1, c - 1


def oj_main():
    # 数字输入 start ===========================
    h, w = [int(i) for i in input().split()]

    board: List[List[str]] = []
    for _ in range(h):
        row = [ch for ch in input()]
        board.append(row)

    res = painting_steps(board)
    print(res)


if __name__ == '__main__':
    # 多用例输入
    # 单用例也可以用
    while True:
        try:
            oj_main()
        except EOFError:
            break
