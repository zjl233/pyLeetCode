from utils.listnode import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        count = 1
        eh = et = ListNode()
        oh = ot = ListNode()

        while head:
            if count % 2 == 0:
                et.next = head
                et = et.next
            else:
                ot.next = head
                ot = ot.next
            head = head.next
            count += 1

        et.next = None
        ot.next = eh.next

        return oh.next
