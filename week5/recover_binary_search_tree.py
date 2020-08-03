# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils.treenode import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(float('-inf'))
        x, y = None, None

        def inorder(node: TreeNode) -> None:
            nonlocal prev, x, y

            if not node:
                return

            inorder(node.left)

            if prev.val > node.val:
                y = node
                if not x:
                    x = prev

            prev = node

            inorder(node.right)

        inorder(root)

        x.val, y.val = y.val, x.val
