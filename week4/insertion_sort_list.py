from typing import List

from utils.listnode import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        prev = dummy
        cur = head
        while cur:
            # <= 为了稳定排序，用 3->3->3 里例子看一下
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next

            # 找到插入位置，插入新节点
            cur.next, prev.next, cur = prev.next, cur, cur.next

            # 将 prev 放到开头
            prev = dummy

        return dummy.next
