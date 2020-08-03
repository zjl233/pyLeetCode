from utils.listnode import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 洗数据
        if not head:
            return head

        # 快慢指针法，快指针先走 k 步
        # 结果返回慢指针

        # 注意 k > 链表长度的情况
        fast = head
        for _ in range(k):
            if not fast:
                return fast
            fast = fast.next

        # 注意更新 slow 和 fast
        slow = head
        while fast:
            slow, fast = slow.next, fast.next

        return slow
