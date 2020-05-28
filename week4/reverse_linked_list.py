from utils.listnode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None

        return first

