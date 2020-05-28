from utils.listnode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tail = self.reverseList(slow)
        while tail is not None:
            if head.val != tail.val:
                return False
            head, tail = head.next, tail.next

        return True

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
