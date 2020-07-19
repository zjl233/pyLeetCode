from typing import Optional

from utils.listnode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast, slow = fast.next, slow.next
                return fast

        return None

