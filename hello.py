# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import deepcopy
from typing import NamedTuple

from week5.test import TreeNode


# Info = namedtuple("Info", [])
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


if __name__ == '__main__':
    l1 = [Element(1), Element(2)]
    l2 = l1.copy()
    l3 = deepcopy(l1)

    print(id(l1[0]))
    print(id(l2[0]))
    print(id(l3[0]))

    print(l1 == l2)
    print(l1 == l3)
