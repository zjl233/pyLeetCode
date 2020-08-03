from utils.listnode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 洗数据
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next

        return dummy.next
