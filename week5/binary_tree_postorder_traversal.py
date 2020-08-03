from typing import List

from utils.treenode import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.append(cur.left) if cur.left else None
            stack.append(cur.right) if cur.right else None
        res.reverse()
        return res

    # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    def postorderTraversalColor(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        stack = [root]
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.extend([cur.val, cur.right, cur.left])
            elif isinstance(cur, int):
                ans.append(cur)
        return ans

    def postorderTraversalMirrors(self, root: TreeNode) -> List[int]:
        vals: List[int] = []
        if not root:
            return vals

        cur = root
        while cur:
            if cur.left:  # 有左子树
                mr = cur.left
                while mr.right and mr.right is not cur:
                    mr = mr.right

                if not mr.right:  # 第一次来
                    mr.right = cur
                    cur = cur.left
                else:  # 第二次来
                    mr.right = None

                    # 反转左子树的右边界
                    head = self.reverse_right_edge(cur.left)
                    # 收集右边界
                    p = head
                    while p:
                        vals.append(p.val)
                        p = p.right
                    self.reverse_right_edge(head)

                    cur = cur.right
            else:  # 没有左子树
                cur = cur.right

        # 反转左子树的右边界
        head = self.reverse_right_edge(root)
        # 收集右边界
        p = head
        while p:
            vals.append(p.val)
            p = p.right
        self.reverse_right_edge(head)

        return vals

    # 反转数的右边界，并返回新的 head
    def reverse_right_edge(self, head: TreeNode) -> TreeNode:
        if not head:
            return head

        prev = None
        cur = head

        while cur:
            cur.right, prev, cur = prev, cur, cur.right

        return prev


