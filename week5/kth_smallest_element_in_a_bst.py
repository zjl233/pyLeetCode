from typing import List

from utils.treenode import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node: TreeNode) -> List[int]:
            if not node:
                return []

            l = inorder(node.left)
            r = inorder(node.right)

            return l + [node.val] + r

        nums = inorder(root)
        return nums[k - 1]
