from typing import Optional

from utils.listnode import ListNode
from utils.treenode import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> Optional[TreeNode]:
        # 洗数据
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        res = self.process(head)
        return res

    def process(self, head) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # 先得到 链表的 left_mid 节点
        left_mid = self.get_left_mid(head)
        mid = left_mid.next
        root = TreeNode(mid.val)
        # 将链表分为两段 left half and right half
        lh = head
        rh = mid.next
        left_mid.next = None
        # 递归
        root.left = self.process(lh)
        root.right = self.process(rh)

        return root

    def get_left_mid(self, head) -> ListNode:
        # 不接受空节点和单节点
        if not head or not head.next:
            raise ValueError('list must have at least two element')

        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow

