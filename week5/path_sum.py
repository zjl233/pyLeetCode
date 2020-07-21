# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.treenode import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
        # if not root and sum_ == 0:
        #    return True
        if not root:
            return False

        if not root.left and not root.right:
            if root.val == sum_:
                return True
            else:
                return False

        return self.hasPathSum(root.left, sum_ - root.val) or self.hasPathSum(root.right, sum_ - root.val)
