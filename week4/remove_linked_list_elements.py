from utils.listnode import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        prev = dummy = ListNode(-1)
        dummy.next = head
        while prev and prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next
