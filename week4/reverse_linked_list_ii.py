from utils.listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        for _ in range(m):
            slow = slow.next

        # 反转链表模板
        prev = fast.next
        cur = slow
        while prev != fast:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 现在 prev 是反转后，链表的头节点
        # 需要将反转之后的链表，接回原链表
        cur = dummy
        for _ in range(m - 1):
            cur = cur.next
        cur.next = prev

        return dummy.next

