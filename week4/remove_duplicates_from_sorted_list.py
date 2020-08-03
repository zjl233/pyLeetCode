from utils.listnode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 洗数据
        if not head or not head.next:
            return head

        # 不用哑节点
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
