# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import string
from typing import NamedTuple

# Info = namedtuple("Info", [])
from utils.treenode import TreeNode


class Info(NamedTuple):  # inherit from typing.NamedTuple
    is_root: bool = False
    sm: int = 0


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        info = self.process(root)
        return info[1]

    def process(self, root: TreeNode) -> Info:
        # info [is_leaf, sum]
        if not root:
            return Info(False, 0)
        if not root.left and not root.right:
            return Info(True, 0)
        sm = 0
        linfo = self.process(root.left)
        rinfo = self.process(root.right)
        if linfo.is_root:
            sm += root.left.val
        sm += linfo.sm
        sm += rinfo.sm
        return Info(False, sm)


class Element:

    def __init__(self, v: int) -> None:
        self.v = v


def f(e: Element):
    print("<<<<f>>>>>>")
    print(id(e))
    e1 = Element(-1)
    e = e1
    print(id(e))
    print("<<<<f>>>>>>")


# 输出到大于 n 为止
def fib(n: int) -> int:
    if n < 2:
        return n

    a, b = 0, 1
    # for i in range(2, n + 1):
    #     a, b = b, a + b

    while b < 2:
        a, b = b, a + b

    return b


if __name__ == '__main__':
    dp = [[[0 for r in range(10)] for c in range(20)] for h in range(30)]
    print(len(dp))
    print(len(dp[0]))
    print(len(dp[0][0]))
    s = "hello"
    print(list(s))
