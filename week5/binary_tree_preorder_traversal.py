from typing import List

from utils.treenode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.append(cur.right) if cur.right else None
            stack.append(cur.left) if cur.left else None
        return res

    def preorderTraversalRecusive(self, root: TreeNode) -> List[int]:
        ans = []
        if root:
            ans.append(root.val)
            ans += self.preorderTraversalRecusive(root.left)
            ans += self.preorderTraversalRecusive(root.right)
        return ans

    # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    def preorderTraversalColor(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        stack = [root]
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.left, cur.val])
            elif isinstance(cur, int):
                ans.append(cur)
        return ans

    def preorderTraversalMorris(self, root: TreeNode) -> List[int]:
        vals = []
        if not root:
            return vals

        cur = root
        while cur:
            if cur.left:  # 有左子树
                mr = cur.left
                while mr.right and mr.right is not cur:
                    mr = mr.right
                if mr.right is None:  # 第一次来
                    vals.append(cur.val)
                    mr.right = cur
                    cur = cur.left
                else:  # 第二次来
                    mr.right = None
                    cur = cur.right
            else:
                cur = cur.right

        return vals
