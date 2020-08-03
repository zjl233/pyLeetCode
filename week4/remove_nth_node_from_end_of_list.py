from utils.listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        # 找到倒数 n + 1 的节点
        for _ in range(n + 1):
            # n 一定有效，所以这里无需判空
            fast = fast.next

        slow = dummy
        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next

