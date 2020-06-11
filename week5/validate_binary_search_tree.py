from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    # 空节点返回的 info
    is_bst: bool = True
    min_: int = float('inf')
    max_: int = float('-inf')


#

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        info = self.process(root)
        return info[0]

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)
        is_bst = l.is_bst and r.is_bst and (l.max_ < root.val < r.min_)  # <= <=
        min_ = l.min_ if l.min_ != float('inf') else root.val
        max_ = r.max_ if r.max_ != float('-inf') else root.val
        return Info(is_bst, min_, max_)
