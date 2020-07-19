from typing import Tuple

from utils.listnode import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 洗数据
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur:
            start = cur.next
            # 将 start, end 置于 k 个节点的开头和末尾
            end = cur
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            nxt = end.next

            # 将翻转后
            start, end = self.reversList(start, end)
            cur.next = start
            end.next = nxt

            # 进入下一轮
            cur = end

        return dummy.next

    def reversList(self, start: ListNode, end: ListNode) -> Tuple[ListNode, ListNode]:
        prev = None
        cur = start
        while prev != end:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return end, start

