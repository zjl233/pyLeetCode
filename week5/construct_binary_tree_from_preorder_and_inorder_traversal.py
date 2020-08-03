from typing import List, Optional

from utils.treenode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        v = preorder.pop(0)
        i = inorder.index(v)

        root = TreeNode(v)
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i + 1:])

        return root

