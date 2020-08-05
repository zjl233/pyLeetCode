# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from utils.treenode import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        # 触底，转向，右子树
        node = self.stack.pop()
        res = node.val
        self.root = node.right
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack is not None or self.root is not None

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        # 不用提前将 root 放入 stack
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            # 触底，转向，右子树
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()